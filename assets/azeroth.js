// azeroth.js: the backdrop behind willhsu.dev.
// Three procedural Azeroth zones rendered with three.js on a fixed canvas behind the page.
// Loaded lazily by the inline script next to <canvas class="backdrop"> in each page.
// Events: dispatches "scenechange" {name, n, of, accent}; listens for "scenestep" to move on.
// Query ?scene=N (1-based) or ?scene=darkshore picks a zone; the order and position persist for the tab.

import * as THREE from 'https://cdnjs.cloudflare.com/ajax/libs/three.js/0.170.0/three.module.min.js';

const TAU = Math.PI * 2;
const rand = (a, b) => a + Math.random() * (b - a);
const hash = (a, b) => { const s = Math.sin(a * 127.1 + b * 311.7) * 43758.5453; return s - Math.floor(s); };
const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };

// ---------- shared textures ----------
let glowTex, discTex;
function glow() {
  if (glowTex) return glowTex;
  const c = document.createElement('canvas'); c.width = c.height = 64;
  const g = c.getContext('2d');
  const grd = g.createRadialGradient(32, 32, 0, 32, 32, 32);
  grd.addColorStop(0, 'rgba(255,255,255,1)');
  grd.addColorStop(0.3, 'rgba(255,255,255,0.5)');
  grd.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = grd; g.fillRect(0, 0, 64, 64);
  glowTex = new THREE.CanvasTexture(c);
  return glowTex;
}
function disc() {
  if (discTex) return discTex;
  const c = document.createElement('canvas'); c.width = c.height = 128;
  const g = c.getContext('2d');
  const grd = g.createRadialGradient(64, 64, 0, 64, 64, 64);
  grd.addColorStop(0, 'rgba(255,255,255,1)');
  grd.addColorStop(0.88, 'rgba(255,255,255,1)');
  grd.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = grd; g.fillRect(0, 0, 128, 128);
  discTex = new THREE.CanvasTexture(c);
  return discTex;
}

// ---------- glowing points (wisps, embers, stars) ----------
const POINT_VERT = `
  attribute float aSize; attribute float aPhase;
  uniform float uTime, uScale, uFlicker, uFar;
  varying float vA;
  void main() {
    vec4 mv = modelViewMatrix * vec4(position, 1.0);
    float dist = -mv.z;
    float pulse = 1.0 - uFlicker * (0.5 + 0.5 * sin(uTime * 2.0 + aPhase * 7.0));
    vA = pulse * (1.0 - smoothstep(uFar * 0.5, uFar, dist));
    gl_PointSize = clamp(aSize * uScale / max(dist, 0.5), 1.0, 96.0);
    gl_Position = projectionMatrix * mv;
  }`;
const POINT_FRAG = `
  uniform vec3 uColor; uniform sampler2D uMap; uniform float uOpacity;
  varying float vA;
  void main() {
    float a = texture2D(uMap, gl_PointCoord).a * vA * uOpacity;
    if (a < 0.004) discard;
    gl_FragColor = vec4(uColor, a);
  }`;

class GlowPoints {
  constructor(n, { color = 0xffffff, size = [0.3, 0.8], flicker = 0.6, far = 80, opacity = 1 } = {}) {
    const geo = new THREE.BufferGeometry();
    this.n = n;
    this.pos = new Float32Array(n * 3);
    const sizes = new Float32Array(n), phases = new Float32Array(n);
    for (let i = 0; i < n; i++) { sizes[i] = rand(size[0], size[1]); phases[i] = rand(0, TAU); }
    geo.setAttribute('position', new THREE.BufferAttribute(this.pos, 3));
    geo.setAttribute('aSize', new THREE.BufferAttribute(sizes, 1));
    geo.setAttribute('aPhase', new THREE.BufferAttribute(phases, 1));
    this.mat = new THREE.ShaderMaterial({
      uniforms: {
        uTime: { value: 0 }, uScale: { value: 400 }, uFlicker: { value: flicker }, uFar: { value: far },
        uColor: { value: new THREE.Color(color) }, uMap: { value: glow() }, uOpacity: { value: opacity },
      },
      vertexShader: POINT_VERT, fragmentShader: POINT_FRAG,
      transparent: true, depthWrite: false, blending: THREE.AdditiveBlending,
    });
    this.mesh = new THREE.Points(geo, this.mat);
    this.mesh.frustumCulled = false;
  }
  set(i, x, y, z) { const o = i * 3; this.pos[o] = x; this.pos[o + 1] = y; this.pos[o + 2] = z; }
  commit() { this.mesh.geometry.attributes.position.needsUpdate = true; }
  update(t, io) { this.mat.uniforms.uTime.value = t; this.mat.uniforms.uScale.value = io.height * 0.5; }
}

function makeStars(n, radius) {
  const s = new GlowPoints(n, { color: 0xd8e2ff, size: [0.7, 1.8], flicker: 0.75, far: 1e6, opacity: 0.9 });
  for (let i = 0; i < n; i++) {
    const th = rand(0, TAU), ph = Math.acos(rand(0.04, 1));
    s.set(i, radius * Math.sin(ph) * Math.cos(th), radius * Math.cos(ph), radius * Math.sin(ph) * Math.sin(th));
  }
  s.commit();
  return s;
}

function makeMoon({ color = 0xe6ecff, halo = 0x8fa4ff, size = 18, haloSize = 110, opacity = 0.45 } = {}) {
  const g = new THREE.Group();
  const h = new THREE.Sprite(new THREE.SpriteMaterial({ map: glow(), color: halo, fog: false, depthWrite: false, transparent: true, blending: THREE.AdditiveBlending, opacity }));
  h.scale.setScalar(haloSize);
  const d = new THREE.Sprite(new THREE.SpriteMaterial({ map: disc(), color, fog: false, depthWrite: false, transparent: true }));
  d.scale.setScalar(size);
  g.add(h, d);
  return g;
}

function disposeScene(scene) {
  scene.traverse(o => {
    if (o.geometry) o.geometry.dispose();
    const mats = Array.isArray(o.material) ? o.material : o.material ? [o.material] : [];
    for (const m of mats) m.dispose();
  });
}

// ---------- zone 1: Teldrassil, under the World Tree at night ----------
let beamTex;
function beamTexture() {
  if (beamTex) return beamTex;
  const c = document.createElement('canvas'); c.width = 4; c.height = 64;
  const g = c.getContext('2d');
  const grd = g.createLinearGradient(0, 0, 0, 64);
  grd.addColorStop(0, 'rgba(255,255,255,0)');
  grd.addColorStop(1, 'rgba(255,255,255,1)');
  g.fillStyle = grd; g.fillRect(0, 0, 4, 64);
  beamTex = new THREE.CanvasTexture(c);
  return beamTex;
}

function teldrassil({ mobile }) {
  const scene = new THREE.Scene();
  const FOG = 0x1b1142;
  scene.background = new THREE.Color(FOG);
  scene.fog = new THREE.FogExp2(FOG, mobile ? 0.03 : 0.021);
  const camera = new THREE.PerspectiveCamera(58, 1, 0.1, 700);
  camera.position.set(0, 3.4, 0);
  scene.add(new THREE.HemisphereLight(0xc47ef0, 0x140a2e, 1.8));
  const moonLight = new THREE.DirectionalLight(0xd6dcff, 1.8);
  moonLight.position.set(-30, 50, -70);
  scene.add(moonLight);

  const SPAN = 180;
  const dummy = new THREE.Object3D();
  const color = new THREE.Color();
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(600, 600), new THREE.MeshStandardMaterial({ color: 0x1a1448, roughness: 1 }));
  ground.rotation.x = -Math.PI / 2;
  scene.add(ground);

  // trees: tall trunks with root flares and broad pink canopies, two tiers of foliage
  const N = mobile ? 70 : 120;
  const trunkGeo = new THREE.CylinderGeometry(0.45, 1.0, 30, 8, 1); trunkGeo.translate(0, 15, 0);
  const rootGeo = new THREE.ConeGeometry(2.4, 4.5, 7, 1); rootGeo.translate(0, 2.25, 0);
  const barkMat = new THREE.MeshStandardMaterial({ color: 0x3b2d62, roughness: 1 });
  const trunks = new THREE.InstancedMesh(trunkGeo, barkMat, N);
  const roots = new THREE.InstancedMesh(rootGeo, barkMat, N);
  const canopies = new THREE.InstancedMesh(new THREE.IcosahedronGeometry(1, 1), new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 1, flatShading: true }), N * 3);
  trunks.frustumCulled = roots.frustumCulled = canopies.frustumCulled = false;
  const PINKS = [0x8c3fae, 0xa553c6, 0xb866d6, 0x7a3a9c, 0xcf7ed8, 0x9f4fc0];
  const pickX = () => { let x; do { x = rand(-80, 80); } while (Math.abs(x) < 9 || (Math.abs(x) > 12 && Math.abs(x) < 21)); return x; };
  const newTree = z => ({
    x: pickX(), z, s: rand(0.8, 1.6), r: rand(0, TAU),
    blobs: [0, 1, 2].map(k => ({ dx: rand(-5, 5), dy: k < 2 ? rand(-2, 2) : rand(-14, -9), dz: rand(-5, 5), sx: rand(7, 12), sy: rand(3.5, 5.5), sz: rand(7, 12), ry: rand(0, TAU), c: PINKS[Math.floor(Math.random() * PINKS.length)] })),
  });
  const trees = [];
  const setTree = i => {
    const tr = trees[i];
    dummy.position.set(tr.x, 0, tr.z); dummy.rotation.set(0, tr.r, 0); dummy.scale.setScalar(tr.s); dummy.updateMatrix();
    trunks.setMatrixAt(i, dummy.matrix); roots.setMatrixAt(i, dummy.matrix);
    const top = 30 * tr.s;
    tr.blobs.forEach((b, k) => {
      dummy.position.set(tr.x + b.dx * tr.s, top + b.dy * tr.s, tr.z + b.dz * tr.s);
      dummy.rotation.set(0, b.ry, 0); dummy.scale.set(b.sx * tr.s, b.sy * tr.s, b.sz * tr.s); dummy.updateMatrix();
      canopies.setMatrixAt(i * 3 + k, dummy.matrix);
      canopies.setColorAt(i * 3 + k, color.setHex(b.c));
    });
  };
  for (let i = 0; i < N; i++) { trees.push(newTree(rand(-SPAN, 12))); setTree(i); }
  trunks.instanceMatrix.needsUpdate = roots.instanceMatrix.needsUpdate = canopies.instanceMatrix.needsUpdate = true;
  canopies.instanceColor.needsUpdate = true;
  scene.add(trunks, roots, canopies);

  // grass
  const GN = mobile ? 400 : 1500;
  const bladeGeo = new THREE.ConeGeometry(0.07, 1.0, 3); bladeGeo.translate(0, 0.5, 0);
  const grass = new THREE.InstancedMesh(bladeGeo, new THREE.MeshStandardMaterial({ color: 0x4a4cae, emissive: 0x15163a, roughness: 1 }), GN);
  grass.frustumCulled = false;
  const blades = [];
  const newBlade = z => ({ x: rand(-34, 34), z, s: rand(0.5, 1.3), r: rand(0, TAU) });
  const setBlade = i => { const b = blades[i]; dummy.position.set(b.x, 0, b.z); dummy.rotation.set(0, b.r, 0); dummy.scale.setScalar(b.s); dummy.updateMatrix(); grass.setMatrixAt(i, dummy.matrix); };
  for (let i = 0; i < GN; i++) { blades.push(newBlade(rand(-SPAN, 12))); setBlade(i); }
  grass.instanceMatrix.needsUpdate = true;
  scene.add(grass);

  // night elf lamp posts along the path; a few real lights follow the nearest ones
  const LN = 8, LGAP = 24;
  const lampMat = new THREE.MeshStandardMaterial({ color: 0x2b2452, roughness: 0.8, metalness: 0.3 });
  const haloMat = new THREE.SpriteMaterial({ map: glow(), color: 0xb48cff, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.55 });
  const lamps = [];
  for (let i = 0; i < LN; i++) {
    const side = i % 2 ? 1 : -1;
    const g = new THREE.Group();
    const post = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.16, 4.6, 7), lampMat); post.position.y = 2.3;
    const arm = new THREE.Mesh(new THREE.BoxGeometry(1.1, 0.08, 0.08), lampMat); arm.position.set(side * -0.45, 4.5, 0);
    const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.28, 10, 10), new THREE.MeshBasicMaterial({ color: 0xe8d8ff })); bulb.position.set(side * -0.9, 4.1, 0);
    const halo = new THREE.Sprite(haloMat); halo.scale.setScalar(4.5); halo.position.copy(bulb.position);
    g.add(post, arm, bulb, halo);
    g.position.set(side * 6.8, 0, -(10 + i * LGAP));
    lamps.push(g); scene.add(g);
  }
  const lampLights = [0, 1, 2].map(() => { const l = new THREE.PointLight(0xb48cff, 16, 15, 2); scene.add(l); return l; });

  // moonwells: a stone basin, glowing water, a column of light and sparks rising
  const MW = 2, MWGAP = 95;
  const wells = [];
  const wellHalo = new THREE.SpriteMaterial({ map: glow(), color: 0x7fe8ff, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.35 });
  for (let i = 0; i < MW; i++) {
    const g = new THREE.Group();
    const basin = new THREE.Mesh(new THREE.CylinderGeometry(3.4, 3.8, 0.9, 24), new THREE.MeshStandardMaterial({ color: 0x8080a8, roughness: 0.9 })); basin.position.y = 0.45;
    const water = new THREE.Mesh(new THREE.CircleGeometry(3.0, 24), new THREE.MeshBasicMaterial({ color: 0x9df2ff })); water.rotation.x = -Math.PI / 2; water.position.y = 0.92;
    const beam = new THREE.Mesh(new THREE.CylinderGeometry(2.0, 2.9, 18, 20, 1, true), new THREE.MeshBasicMaterial({ color: 0x8fe9ff, map: beamTexture(), transparent: true, opacity: 0.22, blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide, fog: false })); beam.position.y = 9.9;
    const light = new THREE.PointLight(0x7fe8ff, 90, 34, 2); light.position.y = 3;
    const halo = new THREE.Sprite(wellHalo); halo.scale.setScalar(12); halo.position.y = 1.5;
    g.add(basin, water, beam, light, halo);
    g.position.set(i % 2 ? 16 : -16, 0, -(40 + i * MWGAP));
    wells.push(g); scene.add(g);
  }
  const SKN = 80;
  const sparks = new GlowPoints(SKN, { color: 0xbff4ff, size: [0.15, 0.4], flicker: 0.7, far: 80 });
  const spark = [];
  for (let i = 0; i < SKN; i++) spark.push({ a: rand(0, TAU), r: rand(0.3, 2.6), y: rand(1, 12), v: rand(0.6, 1.6) });
  scene.add(sparks.mesh);

  // wisps between the trees, petals drifting down
  const WN = mobile ? 60 : 120;
  const wisps = new GlowPoints(WN, { color: 0xcfe9ff, size: [0.5, 1.3], flicker: 0.85, far: 90 });
  const wbase = [];
  for (let i = 0; i < WN; i++) wbase.push({ x: rand(-40, 40), y: rand(0.8, 10), z: rand(-SPAN, 10), p: rand(0, TAU) });
  scene.add(wisps.mesh);
  const PN = mobile ? 80 : 200;
  const petals = new GlowPoints(PN, { color: 0xff9fdc, size: [0.12, 0.3], flicker: 0.3, far: 60, opacity: 0.75 });
  const petal = [];
  for (let i = 0; i < PN; i++) petal.push({ x: rand(-30, 30), y: rand(0, 26), z: rand(-SPAN, 10), v: rand(0.4, 0.9), p: rand(0, TAU) });
  scene.add(petals.mesh);

  const stars = makeStars(mobile ? 100 : 180, 420);
  stars.mat.uniforms.uOpacity.value = 0.4;
  scene.add(stars.mesh);
  const moon = makeMoon({ color: 0xf2ecff, size: 24, haloSize: 240, opacity: 0.55, halo: 0xb08cff });
  scene.add(moon);

  let dist = 0;
  const look = new THREE.Vector3();
  function update(t, dt, io) {
    dist += dt * 1.5;
    const cz = -dist;
    const sway = Math.sin(t * 0.22) * 1.3;
    camera.position.set(sway + io.pointer.x * 1.4, 3.4 + Math.sin(t * 0.9) * 0.08 - io.pointer.y * 0.5, cz);
    look.set(sway * 0.4 + io.pointer.x * 3.5, 7.2 - io.pointer.y * 1.8 - io.scroll * 2.4, cz - 22);
    camera.lookAt(look);
    ground.position.z = cz;
    stars.mesh.position.copy(camera.position);
    moon.position.set(camera.position.x - 60, 100, cz - 230);

    let dirty = false;
    for (let i = 0; i < N; i++) if (trees[i].z > cz + 14) { trees[i] = newTree(trees[i].z - SPAN - 26); setTree(i); dirty = true; }
    if (dirty) { trunks.instanceMatrix.needsUpdate = roots.instanceMatrix.needsUpdate = canopies.instanceMatrix.needsUpdate = true; canopies.instanceColor.needsUpdate = true; }
    dirty = false;
    for (let i = 0; i < GN; i++) if (blades[i].z > cz + 6) { blades[i] = newBlade(blades[i].z - SPAN - 18); setBlade(i); dirty = true; }
    if (dirty) grass.instanceMatrix.needsUpdate = true;

    for (const g of lamps) if (g.position.z > cz + 6) g.position.z -= LN * LGAP;
    const nearLamps = lamps.filter(g => g.position.z < cz + 4).sort((a, b) => b.position.z - a.position.z);
    lampLights.forEach((l, i) => { const g = nearLamps[i]; if (g) { l.position.set(g.position.x * 0.85, 4.1, g.position.z); l.intensity = 16; } else l.intensity = 0; });

    for (const g of wells) if (g.position.z > cz + 12) { g.position.z -= MW * MWGAP; g.position.x = Math.random() < 0.5 ? -16 : 16; }
    for (let i = 0; i < SKN; i++) {
      const s = spark[i], w = wells[i % MW];
      s.y += s.v * dt; s.a += dt * 0.4;
      if (s.y > 13) s.y = 1;
      sparks.set(i, w.position.x + Math.cos(s.a) * s.r, s.y, w.position.z + Math.sin(s.a) * s.r);
    }
    sparks.commit(); sparks.update(t, io);

    for (let i = 0; i < WN; i++) {
      const w = wbase[i];
      if (w.z > cz + 6) { w.z -= SPAN + 10; w.x = rand(-40, 40); }
      wisps.set(i, w.x + Math.sin(t * 0.6 + w.p) * 1.4, w.y + Math.sin(t * 0.8 + w.p * 1.3) * 0.7, w.z);
    }
    wisps.commit(); wisps.update(t, io);
    for (let i = 0; i < PN; i++) {
      const p = petal[i];
      p.y -= p.v * dt; p.x += Math.sin(t * 0.9 + p.p) * 0.6 * dt;
      if (p.y < 0) { p.y = 26; p.x = rand(-30, 30); }
      if (p.z > cz + 4) p.z -= SPAN;
      petals.set(i, p.x, p.y, p.z);
    }
    petals.commit(); petals.update(t, io); stars.update(t, io);
  }
  return { name: 'teldrassil.lua', accent: '#a78bfa', scene, camera, update };
}

// ---------- zone 2: Darkshore, the coast at night in the rain ----------
function darkshore({ mobile }) {
  const scene = new THREE.Scene();
  const BASE = new THREE.Color(0x04070f), WHITE = new THREE.Color(0xdfe8ff);
  scene.background = new THREE.Color(BASE);
  scene.fog = new THREE.Fog(scene.background, 60, 260);
  const camera = new THREE.PerspectiveCamera(55, 1, 0.1, 900);
  camera.position.set(0, 6, 0);

  const hemi = new THREE.HemisphereLight(0x34487a, 0x05070c, 0.8);
  scene.add(hemi);
  const moonDir = new THREE.Vector3(-175, 88, -260).normalize();
  const moonLight = new THREE.DirectionalLight(0xbccbff, 1.3);
  moonLight.position.copy(moonDir).multiplyScalar(100);
  scene.add(moonLight);

  // sea: sines in the vertex shader, moon glitter in the fragment
  const segs = mobile ? 80 : 150;
  const seaGeo = new THREE.PlaneGeometry(700, 700, segs, segs); seaGeo.rotateX(-Math.PI / 2);
  const seaMat = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 }, uMoonDir: { value: moonDir }, uCam: { value: camera.position },
      uDeep: { value: new THREE.Color(0x050b1a) }, uShallow: { value: new THREE.Color(0x0e2447) },
      uFogColor: { value: scene.fog.color }, uFogNear: { value: 60 }, uFogFar: { value: 260 },
    },
    vertexShader: `
      uniform float uTime; varying vec3 vWorld; varying vec3 vNormal; varying float vCrest;
      void wave(vec2 p, vec2 d, float w, float a, float s, inout float h, inout vec2 g) {
        float ph = dot(d, p) * w + uTime * s; h += a * sin(ph); g += d * (w * a * cos(ph));
      }
      void main() {
        vec3 pos = position; vec2 p = pos.xz; float h = 0.0; vec2 g = vec2(0.0);
        wave(p, normalize(vec2(0.3, 1.0)), 0.16, 0.6, 1.0, h, g);
        wave(p, normalize(vec2(-0.6, 1.0)), 0.3, 0.32, 1.5, h, g);
        wave(p, normalize(vec2(1.0, 0.4)), 0.55, 0.14, 2.2, h, g);
        wave(p, normalize(vec2(-0.2, -1.0)), 0.95, 0.07, 3.0, h, g);
        pos.y += h; vCrest = h;
        vNormal = normalize(vec3(-g.x, 1.0, -g.y));
        vec4 w = modelMatrix * vec4(pos, 1.0); vWorld = w.xyz;
        gl_Position = projectionMatrix * viewMatrix * w;
      }`,
    fragmentShader: `
      uniform vec3 uMoonDir, uCam, uDeep, uShallow, uFogColor; uniform float uFogNear, uFogFar;
      varying vec3 vWorld; varying vec3 vNormal; varying float vCrest;
      void main() {
        vec3 N = normalize(vNormal); vec3 V = normalize(uCam - vWorld);
        float fres = pow(1.0 - max(dot(N, V), 0.0), 3.0);
        vec3 col = mix(uDeep, uShallow, smoothstep(-0.7, 1.0, vCrest));
        col += vec3(0.3, 0.42, 0.6) * fres * 0.3;
        vec3 H = normalize(uMoonDir + V);
        float nh = max(dot(N, H), 0.0);
        col += vec3(0.85, 0.9, 1.0) * (pow(nh, 220.0) * 1.8 + pow(nh, 26.0) * 0.1);
        float f = smoothstep(uFogNear, uFogFar, distance(uCam, vWorld));
        gl_FragColor = vec4(mix(col, uFogColor, f), 1.0);
      }`,
  });
  const sea = new THREE.Mesh(seaGeo, seaMat);
  sea.position.set(-40, 0, -150);
  scene.add(sea);

  // the shore on the right: a dark shelf, rocks, and the broken columns of an old elven ruin
  const dark = new THREE.MeshStandardMaterial({ color: 0x0b0a12, roughness: 1 });
  const land = new THREE.Mesh(new THREE.BoxGeometry(260, 6, 600), dark);
  land.position.set(150, -2.6, -150);
  scene.add(land);
  const RN = 44;
  const rocks = new THREE.InstancedMesh(new THREE.DodecahedronGeometry(1.4, 0), new THREE.MeshStandardMaterial({ color: 0x0f0d17, roughness: 1, flatShading: true }), RN);
  rocks.frustumCulled = false;
  const dummy = new THREE.Object3D();
  for (let i = 0; i < RN; i++) {
    dummy.position.set(rand(22, 60), rand(-0.6, 0.4), rand(-220, 10));
    dummy.scale.set(rand(0.6, 2.6), rand(0.5, 1.6), rand(0.6, 2.6));
    dummy.rotation.set(rand(0, TAU), rand(0, TAU), 0);
    dummy.updateMatrix(); rocks.setMatrixAt(i, dummy.matrix);
  }
  scene.add(rocks);
  const CN = 9;
  const cols = new THREE.InstancedMesh(new THREE.CylinderGeometry(1.1, 1.3, 1, 8), dark, CN);
  cols.frustumCulled = false;
  for (let i = 0; i < CN; i++) {
    const h = rand(7, 18);
    dummy.position.set(rand(48, 95), h / 2, rand(-200, -70));
    dummy.scale.set(1, h, 1); dummy.rotation.set(0, rand(0, TAU), rand(-0.06, 0.06));
    dummy.updateMatrix(); cols.setMatrixAt(i, dummy.matrix);
  }
  scene.add(cols);

  // dead, wind-bent trees along the shore
  const DT = 26;
  const deadTrunk = new THREE.InstancedMesh(new THREE.CylinderGeometry(0.22, 0.7, 11, 6), dark, DT);
  const deadBranch = new THREE.InstancedMesh(new THREE.CylinderGeometry(0.08, 0.22, 4.5, 5), dark, DT * 2);
  deadTrunk.frustumCulled = deadBranch.frustumCulled = false;
  for (let i = 0; i < DT; i++) {
    const x = rand(28, 92), z = rand(-215, 5), h = rand(0.7, 1.4);
    dummy.position.set(x, 5.5 * h - 0.3, z); dummy.rotation.set(0, rand(0, TAU), rand(-0.14, 0.14)); dummy.scale.setScalar(h); dummy.updateMatrix(); deadTrunk.setMatrixAt(i, dummy.matrix);
    for (let k = 0; k < 2; k++) {
      dummy.position.set(x + rand(-1, 1), (7 + k * 2.2) * h, z + rand(-1, 1));
      dummy.rotation.set(rand(-0.9, 0.9), rand(0, TAU), rand(0.5, 1.1) * (k ? -1 : 1)); dummy.scale.setScalar(h); dummy.updateMatrix();
      deadBranch.setMatrixAt(i * 2 + k, dummy.matrix);
    }
  }
  scene.add(deadTrunk, deadBranch);

  // a wreck beached in the shallows, and a broken mast further out
  const wreck = new THREE.Group();
  const hull = new THREE.Mesh(new THREE.BoxGeometry(6.5, 5, 24), dark); hull.position.y = 1.5; wreck.add(hull);
  const bow = new THREE.Mesh(new THREE.BoxGeometry(4.6, 5, 4.6), dark); bow.position.set(0, 1.5, -12); bow.rotation.y = Math.PI / 4; wreck.add(bow);
  const mast = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.35, 20, 7), dark); mast.position.set(0, 12, -2); mast.rotation.z = 0.25; wreck.add(mast);
  const yard = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 9, 5), dark); yard.rotation.z = Math.PI / 2 + 0.25; yard.position.set(-1.5, 16, -2); wreck.add(yard);
  wreck.position.set(17, -1.4, -98); wreck.rotation.set(0.08, 0.5, 0.32);
  scene.add(wreck);
  const mast2 = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.4, 16, 7), dark); mast2.position.set(-72, 3, -165); mast2.rotation.set(0.2, 0, -0.5);
  scene.add(mast2);

  // low cloud drifting across the moon
  const CL = 7, clouds = [];
  const cloudMat = new THREE.SpriteMaterial({ map: glow(), color: 0x0a0e1b, transparent: true, opacity: 0.9, depthWrite: false, fog: false });
  for (let i = 0; i < CL; i++) {
    const c = new THREE.Sprite(cloudMat); const w = rand(120, 230); c.scale.set(w, w * 0.4, 1);
    c.userData = { x: rand(-300, 300), y: rand(50, 125), z: rand(-215, -170), v: rand(1.5, 3.5) };
    clouds.push(c); scene.add(c);
  }

  // rain
  const DN = mobile ? 220 : 650;
  const rainPos = new Float32Array(DN * 6);
  const drops = [];
  for (let i = 0; i < DN; i++) drops.push({ x: rand(-45, 45), y: rand(0, 40), z: rand(-70, 6), v: rand(16, 24) });
  const setDrop = i => { const d = drops[i], o = i * 6; rainPos[o] = d.x; rainPos[o + 1] = d.y; rainPos[o + 2] = d.z; rainPos[o + 3] = d.x - 0.14; rainPos[o + 4] = d.y + 0.9; rainPos[o + 5] = d.z; };
  const rainGeo = new THREE.BufferGeometry();
  rainGeo.setAttribute('position', new THREE.BufferAttribute(rainPos, 3));
  const rain = new THREE.LineSegments(rainGeo, new THREE.LineBasicMaterial({ color: 0x8ea4cc, transparent: true, opacity: 0.26 }));
  rain.frustumCulled = false;
  scene.add(rain);

  const stars = makeStars(mobile ? 300 : 800, 500);
  scene.add(stars.mesh);
  const moon = makeMoon({ size: 26, haloSize: 220, opacity: 0.5, halo: 0x7f96ff });
  scene.add(moon);

  let flashAt = 6 + rand(0, 16);
  const look = new THREE.Vector3();
  function update(t, dt, io) {
    camera.position.set(io.pointer.x * 1.6, 6 + Math.sin(t * 0.7) * 0.12 - io.pointer.y * 0.8, 0);
    look.set(-36 + Math.sin(t * 0.06) * 14 + io.pointer.x * 10, 3.5 - io.pointer.y * 4 - io.scroll * 4, -120);
    camera.lookAt(look);
    moon.position.copy(moonDir).multiplyScalar(320).add(camera.position);
    stars.mesh.position.copy(camera.position);
    seaMat.uniforms.uTime.value = t;

    // lightning far out over the sea
    let k = 0;
    const f = t - flashAt;
    if (f > 0) {
      if (f < 0.6) k = Math.max(0, Math.sin(f * 24) * Math.exp(-f * 6));
      else flashAt = t + rand(14, 42);
    }
    scene.background.copy(BASE).lerp(WHITE, k * 0.2);
    hemi.intensity = 0.8 + k * 3;
    for (const c of clouds) {
      const u = c.userData; u.x += u.v * dt; if (u.x > 320) u.x = -320;
      c.position.set(camera.position.x + u.x, camera.position.y + u.y, camera.position.z + u.z);
    }

    for (let i = 0; i < DN; i++) {
      const d = drops[i];
      d.y -= d.v * dt; d.x -= 2.6 * dt;
      if (d.y < -1) { d.y += 41; d.x = rand(-45, 45); }
      setDrop(i);
    }
    rainGeo.attributes.position.needsUpdate = true;
    stars.update(t, io);
  }
  return { name: 'darkshore.lua', accent: '#4aa3ff', scene, camera, update };
}

// ---------- zone 3: the Deadmines, a torchlit mine tunnel with cart rails ----------
function vnoise(x, y, z) {
  const xi = Math.floor(x), yi = Math.floor(y), zi = Math.floor(z);
  const h = (a, b, c) => { const s = Math.sin(a * 127.1 + b * 311.7 + c * 74.7) * 43758.5453; return s - Math.floor(s); };
  const sm = t => t * t * (3 - 2 * t);
  const tx = sm(x - xi), ty = sm(y - yi), tz = sm(z - zi);
  const l = (a, b, t) => a + (b - a) * t;
  return l(
    l(l(h(xi, yi, zi), h(xi + 1, yi, zi), tx), l(h(xi, yi + 1, zi), h(xi + 1, yi + 1, zi), tx), ty),
    l(l(h(xi, yi, zi + 1), h(xi + 1, yi, zi + 1), tx), l(h(xi, yi + 1, zi + 1), h(xi + 1, yi + 1, zi + 1), tx), ty), tz) - 0.5;
}

let rockTex;
function rockTexture() {
  if (rockTex) return rockTex;
  const S = 256, c = document.createElement('canvas'); c.width = c.height = S;
  const g = c.getContext('2d'), img = g.createImageData(S, S);
  const octs = [[6, 0.45], [12, 0.25], [24, 0.18], [64, 0.12]].map(([n, w]) => { const a = new Float32Array(n * n); for (let i = 0; i < a.length; i++) a[i] = Math.random(); return { n, w, a }; });
  const sm = t => t * t * (3 - 2 * t);
  for (let y = 0; y < S; y++) for (let x = 0; x < S; x++) {
    let v = 0;
    for (const o of octs) {
      const fx = x / S * o.n, fy = y / S * o.n, x0 = Math.floor(fx), y0 = Math.floor(fy), tx = sm(fx - x0), ty = sm(fy - y0);
      const at = (xx, yy) => o.a[(yy % o.n) * o.n + (xx % o.n)];
      v += o.w * ((at(x0, y0) * (1 - tx) + at(x0 + 1, y0) * tx) * (1 - ty) + (at(x0, y0 + 1) * (1 - tx) + at(x0 + 1, y0 + 1) * tx) * ty);
    }
    const k = Math.round(90 + v * 165), p = (y * S + x) * 4;
    img.data[p] = k; img.data[p + 1] = k; img.data[p + 2] = k; img.data[p + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  rockTex = new THREE.CanvasTexture(c);
  rockTex.wrapS = rockTex.wrapT = THREE.RepeatWrapping;
  rockTex.repeat.set(8, 26);
  rockTex.colorSpace = THREE.SRGBColorSpace;
  return rockTex;
}

let bannerTex;
function bannerTexture() {
  if (bannerTex) return bannerTex;
  const c = document.createElement('canvas'); c.width = 64; c.height = 128;
  const g = c.getContext('2d');
  g.fillStyle = '#7d1414'; g.fillRect(0, 0, 64, 128);
  g.fillStyle = '#5a0d0d'; g.fillRect(0, 0, 64, 9); g.fillRect(0, 60, 64, 3);
  g.fillStyle = '#2a0707'; g.beginPath(); g.moveTo(32, 30); g.lineTo(55, 64); g.lineTo(32, 98); g.lineTo(9, 64); g.closePath(); g.fill();
  g.fillStyle = '#d9c7a0'; g.beginPath(); g.moveTo(32, 46); g.lineTo(44, 64); g.lineTo(32, 82); g.lineTo(20, 64); g.closePath(); g.fill();
  g.globalCompositeOperation = 'destination-out';
  g.beginPath(); g.moveTo(0, 128); g.lineTo(11, 110); g.lineTo(22, 128); g.lineTo(33, 106); g.lineTo(44, 128); g.lineTo(54, 112); g.lineTo(64, 128); g.closePath(); g.fill();
  bannerTex = new THREE.CanvasTexture(c);
  bannerTex.colorSpace = THREE.SRGBColorSpace;
  return bannerTex;
}

function deadmines({ mobile }) {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x060403);
  scene.fog = new THREE.FogExp2(0x060403, mobile ? 0.07 : 0.05);
  const camera = new THREE.PerspectiveCamera(62, 1, 0.05, 300);
  camera.position.set(0, 0.9, 0);
  scene.add(new THREE.AmbientLight(0x3a2a22, 1.0));
  scene.add(new THREE.HemisphereLight(0x2a3a5a, 0x100806, 1.5));
  const fill = new THREE.PointLight(0x8a6048, 7, 18, 2);
  scene.add(fill);
  const deep = new THREE.PointLight(0x2a4a8a, 90, 80, 2);
  scene.add(deep);

  // the tunnel: two rock segments carved with value noise, seamless at the joins, leapfrogging ahead
  const SEG = 120, R = 6, AXIS = 1.5, RINGS = mobile ? 60 : 110, SIDES = mobile ? 18 : 28;
  const carve = (cx, sy, zz) => {
    const at = z => 1.5 * vnoise(cx * 1.3, sy * 1.3, z * 0.045) + 0.6 * vnoise(cx * 3.2, sy * 3.2, z * 0.16) + 0.22 * vnoise(cx * 9, sy * 9, z * 0.55);
    const w = Math.min(1, zz / 14, (SEG - zz) / 14);
    const ws = w * w * (3 - 2 * w);
    return at(0) * (1 - ws) + at(zz) * ws;
  };
  const wallRadius = (a, z) => { const zz = (((z - 10) % SEG) + SEG) % SEG; return R + carve(Math.cos(a), Math.sin(a), zz); };
  const rockMat = new THREE.MeshStandardMaterial({ color: 0x8a7a6c, map: rockTexture(), bumpMap: rockTexture(), bumpScale: 1.0, roughness: 1, side: THREE.BackSide });
  const makeTube = () => {
    const geo = new THREE.CylinderGeometry(R, R, SEG, SIDES, RINGS, true); geo.rotateX(Math.PI / 2);
    const p = geo.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i), y = p.getY(i), z = p.getZ(i);
      const a = Math.atan2(y, x), cx = Math.cos(a), sy = Math.sin(a);
      const r = R + carve(cx, sy, z + SEG / 2);
      p.setXYZ(i, cx * r, sy * r + AXIS, z);
    }
    geo.computeVertexNormals();
    const m = new THREE.Mesh(geo, rockMat); m.frustumCulled = false; return m;
  };
  const tubes = [makeTube(), makeTube()];
  tubes[0].position.z = 10 - SEG / 2;
  tubes[1].position.z = tubes[0].position.z - SEG;
  scene.add(tubes[0], tubes[1]);

  const floorMat = new THREE.MeshStandardMaterial({ color: 0x4a3c30, map: rockTexture(), bumpMap: rockTexture(), bumpScale: 0.3, roughness: 1 });
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(16, 300), floorMat);
  floor.rotation.x = -Math.PI / 2; floor.position.y = -2.2;
  scene.add(floor);
  const railMat = new THREE.MeshStandardMaterial({ color: 0x8a7a66, roughness: 0.4, metalness: 0.7 });
  const rails = [-0.9, 0.9].map(x => { const r = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.14, 300), railMat); r.position.set(x, -2.1, 0); return r; });
  scene.add(...rails);

  // ties, timber frames, stalactites and rubble: all recycled as the camera passes them
  const dummy = new THREE.Object3D();
  const wood = new THREE.MeshStandardMaterial({ color: 0x4e3a26, roughness: 1 });
  const TN = 150, TIE = 1.6;
  const ties = new THREE.InstancedMesh(new THREE.BoxGeometry(2.4, 0.12, 0.3), new THREE.MeshStandardMaterial({ color: 0x332519, roughness: 1 }), TN);
  const FN = 26, FRAME = 9;
  const posts = new THREE.InstancedMesh(new THREE.BoxGeometry(0.4, 4.6, 0.4), wood, FN * 2);
  const beams = new THREE.InstancedMesh(new THREE.BoxGeometry(9.0, 0.45, 0.45), wood, FN);
  const SN = mobile ? 30 : 70;
  const stalGeo = new THREE.ConeGeometry(0.32, 2.2, 6); stalGeo.rotateX(Math.PI); stalGeo.translate(0, -1.0, 0);
  const rubbleMat = new THREE.MeshStandardMaterial({ color: 0x7a6a5c, map: rockTexture(), roughness: 1, flatShading: true });
  const stals = new THREE.InstancedMesh(stalGeo, rubbleMat, SN);
  const BN = mobile ? 30 : 64;
  const rubble = new THREE.InstancedMesh(new THREE.DodecahedronGeometry(0.5, 0), rubbleMat, BN);
  for (const m of [ties, posts, beams, stals, rubble]) m.frustumCulled = false;
  const tieZ = [], frameZ = [], stal = [], rub = [];
  const setTie = i => { dummy.position.set(0, -2.18, tieZ[i]); dummy.rotation.set(0, 0, 0); dummy.scale.setScalar(1); dummy.updateMatrix(); ties.setMatrixAt(i, dummy.matrix); };
  const setFrame = i => {
    dummy.rotation.set(0, 0, 0); dummy.scale.setScalar(1);
    dummy.position.set(-4.1, 0, frameZ[i]); dummy.updateMatrix(); posts.setMatrixAt(i * 2, dummy.matrix);
    dummy.position.set(4.1, 0, frameZ[i]); dummy.updateMatrix(); posts.setMatrixAt(i * 2 + 1, dummy.matrix);
    dummy.position.set(0, 2.35, frameZ[i]); dummy.updateMatrix(); beams.setMatrixAt(i, dummy.matrix);
  };
  const newStal = z => { const a = rand(-0.95, 0.95); const r = wallRadius(Math.PI / 2 - a, z) - 0.3; return { z, x: Math.sin(a) * r, y: AXIS + Math.cos(a) * r, s: rand(0.5, 1.9), rx: rand(-0.15, 0.15), rz: rand(-0.15, 0.15) }; };
  const setStal = i => { const s = stal[i]; dummy.position.set(s.x, s.y, s.z); dummy.rotation.set(s.rx, 0, s.rz); dummy.scale.set(s.s, s.s, s.s); dummy.updateMatrix(); stals.setMatrixAt(i, dummy.matrix); };
  const newRub = z => { const s = rand(0.35, 1.3); return { z, x: (Math.random() < 0.5 ? -1 : 1) * rand(2.4, 4.8), s, ry: rand(0, TAU) }; };
  const setRub = i => { const r = rub[i]; dummy.position.set(r.x, -2.2 + r.s * 0.3, r.z); dummy.rotation.set(0, r.ry, 0); dummy.scale.set(r.s, r.s * 0.7, r.s); dummy.updateMatrix(); rubble.setMatrixAt(i, dummy.matrix); };
  for (let i = 0; i < TN; i++) { tieZ.push(6 - i * TIE); setTie(i); }
  for (let i = 0; i < FN; i++) { frameZ.push(4 - i * FRAME); setFrame(i); }
  for (let i = 0; i < SN; i++) { stal.push(newStal(rand(-2 * SEG, 6))); setStal(i); }
  for (let i = 0; i < BN; i++) { rub.push(newRub(rand(-2 * SEG, 6))); setRub(i); }
  for (const m of [ties, posts, beams, stals, rubble]) m.instanceMatrix.needsUpdate = true;
  scene.add(ties, posts, beams, stals, rubble);

  // Defias clutter: crates and barrels along the walls, banners hanging from every third frame
  const KN = mobile ? 14 : 30;
  const crates = new THREE.InstancedMesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshStandardMaterial({ color: 0x6a4a2a, map: rockTexture(), roughness: 1 }), KN);
  const RBN = mobile ? 10 : 20;
  const barrels = new THREE.InstancedMesh(new THREE.CylinderGeometry(0.45, 0.45, 1.1, 10), new THREE.MeshStandardMaterial({ color: 0x3e2c1c, roughness: 0.9 }), RBN);
  crates.frustumCulled = barrels.frustumCulled = false;
  const crate = [], barrel = [];
  const eul = new THREE.Euler();
  const newCrate = z => { const sc = rand(0.6, 1.15); return { z, x: (Math.random() < 0.5 ? -1 : 1) * rand(2.9, 4.2), sc, ry: rand(-0.4, 0.4) + (Math.random() < 0.5 ? 0 : Math.PI / 2) }; };
  const setCrate = i => { const k = crate[i]; dummy.position.set(k.x, -2.2 + k.sc / 2, k.z); dummy.rotation.set(0, k.ry, 0); dummy.scale.setScalar(k.sc); dummy.updateMatrix(); crates.setMatrixAt(i, dummy.matrix); };
  const newBarrel = z => ({ z, x: (Math.random() < 0.5 ? -1 : 1) * rand(2.8, 4.3), lying: Math.random() < 0.4, ry: rand(0, TAU) });
  const setBarrel = i => {
    const b = barrel[i]; dummy.scale.setScalar(1);
    if (b.lying) { dummy.position.set(b.x, -2.2 + 0.45, b.z); dummy.setRotationFromEuler(eul.set(Math.PI / 2, b.ry, 0, 'YXZ')); }
    else { dummy.position.set(b.x, -2.2 + 0.55, b.z); dummy.setRotationFromEuler(eul.set(0, b.ry, 0, 'YXZ')); }
    dummy.updateMatrix(); barrels.setMatrixAt(i, dummy.matrix); dummy.rotation.order = 'XYZ';
  };
  for (let i = 0; i < KN; i++) { crate.push(newCrate(rand(-2 * SEG, 6))); setCrate(i); }
  for (let i = 0; i < RBN; i++) { barrel.push(newBarrel(rand(-2 * SEG, 6))); setBarrel(i); }
  crates.instanceMatrix.needsUpdate = barrels.instanceMatrix.needsUpdate = true;
  scene.add(crates, barrels);
  const bannerGeo = new THREE.PlaneGeometry(1.1, 2.4); bannerGeo.translate(0, -1.2, 0);
  const bannerMat = new THREE.MeshStandardMaterial({ map: bannerTexture(), transparent: true, alphaTest: 0.5, side: THREE.DoubleSide, roughness: 1 });
  const banners = [];
  for (let i = 0; i < FN; i += 3) { const b = new THREE.Mesh(bannerGeo, bannerMat); b.userData.frame = i; b.userData.x = (i / 3) % 2 ? 2.4 : -2.4; banners.push(b); scene.add(b); }
  const placeBanner = b => b.position.set(b.userData.x, 2.12, frameZ[b.userData.frame] - 0.3);
  banners.forEach(placeBanner);

  // torches hang on every other frame; a small pool of real lights follows the nearest ones
  const torches = [];
  const flameMat = new THREE.SpriteMaterial({ map: glow(), color: 0xff9a3a, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.9 });
  const hazeMat = new THREE.SpriteMaterial({ map: glow(), color: 0xff7a22, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0.16 });
  for (let i = 0; i < FN; i += 2) {
    const g = new THREE.Group();
    const flame = new THREE.Sprite(flameMat); flame.scale.setScalar(1.6);
    const haze = new THREE.Sprite(hazeMat); haze.scale.setScalar(9);
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.11, 8, 8), new THREE.MeshBasicMaterial({ color: 0xffc070 }));
    const stick = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.8, 5), wood); stick.position.y = -0.45;
    g.add(haze, flame, head, stick);
    g.userData.frame = i; g.userData.side = (i / 2) % 2 ? 1 : -1;
    torches.push(g); scene.add(g);
  }
  const placeTorch = g => g.position.set(g.userData.side * 3.72, 1.1, frameZ[g.userData.frame] - 0.35);
  torches.forEach(placeTorch);
  const LN = 6;
  const lights = [];
  for (let i = 0; i < LN; i++) { const l = new THREE.PointLight(0xff8c38, 55, 30, 2); lights.push(l); scene.add(l); }

  // carts: one rolling ahead with glowing ore, two wrecked beside the rails
  const iron = new THREE.MeshStandardMaterial({ color: 0x4a4038, roughness: 0.7, metalness: 0.5 });
  const makeCart = ore => {
    const g = new THREE.Group();
    const body = new THREE.Mesh(new THREE.BoxGeometry(1.7, 0.95, 2.3), iron); body.position.y = 0.75; g.add(body);
    const rim = new THREE.Mesh(new THREE.BoxGeometry(1.85, 0.12, 2.45), iron); rim.position.y = 1.2; g.add(rim);
    for (const [x, z] of [[-0.95, -0.7], [0.95, -0.7], [-0.95, 0.7], [0.95, 0.7]]) {
      const w = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 0.12, 10), iron); w.rotation.z = Math.PI / 2; w.position.set(x, 0.24, z); g.add(w);
    }
    if (ore) {
      const om = new THREE.MeshStandardMaterial({ color: 0xffb347, emissive: 0xff8c1a, emissiveIntensity: 1.2, roughness: 0.5 });
      for (let i = 0; i < 8; i++) { const o = new THREE.Mesh(new THREE.DodecahedronGeometry(0.22, 0), om); o.position.set(rand(-0.5, 0.5), 1.25 + rand(0, 0.3), rand(-0.8, 0.8)); o.rotation.set(rand(0, TAU), rand(0, TAU), 0); g.add(o); }
      const l = new THREE.PointLight(0xffa040, 8, 7, 2); l.position.y = 1.7; g.add(l);
    }
    return g;
  };
  const rolling = makeCart(true); rolling.position.set(0, -2.03, -18); scene.add(rolling);
  const wrecks = [makeCart(false), makeCart(false)];
  wrecks[0].position.set(2.9, -2.0, -48); wrecks[0].rotation.set(0.1, 0.5, 1.45);
  wrecks[1].position.set(-3.0, -2.1, -118); wrecks[1].rotation.set(-0.05, -0.8, -1.3);
  scene.add(...wrecks);

  const EN = mobile ? 90 : 220;
  const embers = new GlowPoints(EN, { color: 0xff8a3a, size: [0.08, 0.26], flicker: 0.9, far: 45 });
  const eb = [];
  for (let i = 0; i < EN; i++) eb.push({ x: rand(-3.2, 3.2), y: rand(-2, 2.8), z: rand(-110, 4), p: rand(0, TAU) });
  scene.add(embers.mesh);
  const HN = mobile ? 20 : 50;
  const dust = new GlowPoints(HN, { color: 0xa07858, size: [2.2, 4.5], flicker: 0.3, far: 40, opacity: 0.07 });
  const db = [];
  for (let i = 0; i < HN; i++) db.push({ x: rand(-4, 4), y: rand(-1.5, 3), z: rand(-60, 4), p: rand(0, TAU) });
  scene.add(dust.mesh);

  let dist = 0;
  const SPEED = 1.1;
  const look = new THREE.Vector3();
  function update(t, dt, io) {
    dist += dt * SPEED;
    const cz = -dist;
    camera.position.set(Math.sin(t * 0.3) * 0.35 + io.pointer.x * 0.5, 0.9 + Math.sin(t * 1.3) * 0.05 - io.pointer.y * 0.3, cz);
    look.set(io.pointer.x * 2, 0.5 - io.pointer.y * 1.2 - io.scroll * 1.4, cz - 12);
    camera.lookAt(look);
    fill.position.set(camera.position.x, camera.position.y + 0.5, cz - 1);
    deep.position.set(0, 0.5, cz - 48);
    floor.position.z = cz - 100; rails[0].position.z = rails[1].position.z = cz - 100;

    for (const tube of tubes) if (tube.position.z - SEG / 2 > cz + 8) tube.position.z -= 2 * SEG;

    let dirty = false;
    for (let i = 0; i < TN; i++) if (tieZ[i] > cz + 4) { tieZ[i] -= TN * TIE; setTie(i); dirty = true; }
    if (dirty) ties.instanceMatrix.needsUpdate = true;
    dirty = false;
    for (let i = 0; i < FN; i++) if (frameZ[i] > cz + 4) { frameZ[i] -= FN * FRAME; setFrame(i); dirty = true; }
    if (dirty) { posts.instanceMatrix.needsUpdate = beams.instanceMatrix.needsUpdate = true; torches.forEach(placeTorch); banners.forEach(placeBanner); }
    banners.forEach((b, i) => { b.rotation.x = Math.sin(t * 1.3 + i * 1.9) * 0.07; });
    dirty = false;
    for (let i = 0; i < KN; i++) if (crate[i].z > cz + 4) { crate[i] = newCrate(crate[i].z - 2 * SEG - 6); setCrate(i); dirty = true; }
    if (dirty) crates.instanceMatrix.needsUpdate = true;
    dirty = false;
    for (let i = 0; i < RBN; i++) if (barrel[i].z > cz + 4) { barrel[i] = newBarrel(barrel[i].z - 2 * SEG - 6); setBarrel(i); dirty = true; }
    if (dirty) barrels.instanceMatrix.needsUpdate = true;
    dirty = false;
    for (let i = 0; i < SN; i++) if (stal[i].z > cz + 4) { stal[i] = newStal(stal[i].z - 2 * SEG - 6); setStal(i); dirty = true; }
    if (dirty) stals.instanceMatrix.needsUpdate = true;
    dirty = false;
    for (let i = 0; i < BN; i++) if (rub[i].z > cz + 4) { rub[i] = newRub(rub[i].z - 2 * SEG - 6); setRub(i); dirty = true; }
    if (dirty) rubble.instanceMatrix.needsUpdate = true;

    // flicker, and hand the real lights to the nearest torches ahead
    const near = torches.filter(g => g.position.z < cz + 6).sort((a, b) => b.position.z - a.position.z);
    for (let i = 0; i < LN; i++) {
      const g = near[i], l = lights[i];
      if (!g) { l.intensity = 0; continue; }
      const k = g.userData.frame;
      const n = 0.78 + 0.22 * (0.5 * Math.sin(t * 13 + k * 1.7) + 0.5 * Math.sin(t * 7.3 + k * 4.1)) + (Math.random() - 0.5) * 0.08;
      l.position.set(g.position.x * 0.85, g.position.y + 0.15, g.position.z);
      l.intensity = 55 * n;
      g.children[1].scale.setScalar(1.6 * (0.9 + n * 0.2));
    }

    rolling.position.z -= dt * (SPEED - 0.3);
    if (rolling.position.z > cz + 3) rolling.position.z = cz - 70;
    rolling.rotation.x = Math.sin(t * 9) * 0.004;
    for (const w of wrecks) if (w.position.z > cz + 4) w.position.z -= 2 * SEG + rand(0, 40);

    for (let i = 0; i < EN; i++) {
      const e = eb[i];
      e.y += 0.55 * dt; e.x += Math.sin(t * 1.3 + e.p) * 0.25 * dt;
      if (e.y > 2.9) { e.y = rand(-2, -1); e.x = rand(-3.2, 3.2); }
      if (e.z > cz + 2) e.z -= 112;
      embers.set(i, e.x, e.y, e.z);
    }
    embers.commit(); embers.update(t, io);
    for (let i = 0; i < HN; i++) {
      const d = db[i];
      if (d.z > cz + 3) d.z -= 62;
      dust.set(i, d.x + Math.sin(t * 0.2 + d.p) * 0.8, d.y + Math.sin(t * 0.17 + d.p * 2) * 0.5, d.z);
    }
    dust.commit(); dust.update(t, io);
  }
  return { name: 'deadmines.lua', accent: '#ff8000', scene, camera, update };
}

const ZONES = [teldrassil, darkshore, deadmines];

// ---------- the loop ----------
export function start(canvas) {
  const mobile = !matchMedia('(hover: hover) and (pointer: fine)').matches || innerWidth < 700;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas, antialias: !mobile, alpha: false, powerPreference: 'low-power' });
  } catch { return null; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, mobile ? 1 : 1.5));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.35;

  const io = { pointer: { x: 0, y: 0 }, scroll: 0, height: 800 };
  const target = { x: 0, y: 0 };
  if (!mobile) addEventListener('pointermove', e => { target.x = e.clientX / innerWidth * 2 - 1; target.y = e.clientY / innerHeight * 2 - 1; }, { passive: true });

  let order = ZONES.map((_, i) => i), pos = 0;
  try {
    const s = JSON.parse(sessionStorage.getItem('azeroth') || 'null');
    if (s && Array.isArray(s.order) && s.order.length === ZONES.length) { order = s.order; pos = Math.min(ZONES.length - 1, Math.max(0, s.pos | 0)); }
    else shuffle(order);
  } catch { shuffle(order); }
  const q = new URLSearchParams(location.search);
  if (q.has('scene')) {
    const v = q.get('scene');
    const byName = ZONES.findIndex(z => z.name === v);
    const n = byName >= 0 ? byName : Math.min(ZONES.length, Math.max(1, Number(v) || 1)) - 1;
    pos = order.indexOf(n);
  }

  const ctx = { mobile, renderer };
  let zone = null;
  function load() {
    zone = ZONES[order[pos]](ctx);
    zone.camera.aspect = innerWidth / innerHeight; zone.camera.updateProjectionMatrix();
    try { sessionStorage.setItem('azeroth', JSON.stringify({ order, pos })); } catch {}
    dispatchEvent(new CustomEvent('scenechange', { detail: { name: zone.name, n: pos + 1, of: order.length, accent: zone.accent } }));
  }
  function resize() {
    renderer.setSize(innerWidth, innerHeight, false);
    if (zone) { zone.camera.aspect = innerWidth / innerHeight; zone.camera.updateProjectionMatrix(); }
  }
  addEventListener('resize', resize);
  load(); resize();

  const HOLD = 80000, FADE = 650;
  let next = performance.now() + HOLD, fading = null, shown = false, last = performance.now();
  function step(d) {
    if (fading) return;
    fading = { at: performance.now(), d };
    canvas.style.transitionDuration = FADE + 'ms';
    canvas.classList.remove('on');
  }
  addEventListener('scenestep', () => step(1));

  function frame(now) {
    requestAnimationFrame(frame);
    const dt = Math.min((now - last) / 1000, 0.05); last = now;
    const t = now / 1000;
    if (fading && now - fading.at >= FADE) {
      disposeScene(zone.scene);
      pos = (pos + fading.d + order.length) % order.length;
      load();
      fading = null; next = now + HOLD;
      canvas.classList.add('on');
      setTimeout(() => { canvas.style.transitionDuration = ''; }, FADE + 50);
    } else if (!fading && now > next) step(1);
    io.pointer.x += (target.x - io.pointer.x) * 0.04;
    io.pointer.y += (target.y - io.pointer.y) * 0.04;
    io.scroll = Math.min(scrollY / innerHeight, 3);
    io.height = renderer.domElement.height;
    zone.update(t, dt, io);
    renderer.render(zone.scene, zone.camera);
    if (!shown) { shown = true; canvas.classList.add('on'); }
  }
  requestAnimationFrame(frame);
  return { step };
}
