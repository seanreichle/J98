
Ring3D = function(innerRadius, outerRadius, heigth, Segments, Color) {
	if(Color=='') Color = 0x00ffff;
	
    var extrudeSettings = {
        amount: heigth,
        bevelEnabled: false,
        curveSegments: Segments
    };
    var arcShape = new THREE.Shape();
    arcShape.moveTo(outerRadius, 0);
    arcShape.absarc(0, 0, outerRadius, 0, Math.PI * 2, false);

    var holePath = new THREE.Path();
    holePath.moveTo(innerRadius, 0);
    holePath.absarc(0, 0, innerRadius, 0, Math.PI * 2, true);
    arcShape.holes.push(holePath);

    var geometry = new THREE.ExtrudeGeometry(arcShape, extrudeSettings);

    var material = new THREE.MeshPhongMaterial({
        color: Color
    });

    var mesh = new THREE.Mesh(geometry, material);
    mesh.rotation.x = Math.PI / 2;
    mesh.position.y = heigth / 2;

    var object = new THREE.Object3D;
    object.add(mesh);

    return object;
}


var colors = [
    0xFF62B0,
    0x9A03FE,
    0x62D0FF,
    0x48FB0D,
    0xDFA800,
    0xC27E3A,
    0x990099,
    0x9669FE,
    0x23819C,
    0x01F33E,
    0xB6BA18,
    0xFF800D,
    0xB96F6F,
    0x4A9586
];
getRandColor = function() {
	return colors[Math.floor(Math.random() * colors.length)];
}