let scene, camera, renderer, elementDetails;

function init() {
    try {
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('container').appendChild(renderer.domElement);

    camera.position.z = 5;

    animate();
    }  catch (e) {
    alert("WebGL is not supported or is disabled in your browser.");
}


function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

function fetchElementData(atomicNumber) {
    fetch(`/element/${atomicNumber}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                displayElementData(data);
            }
        });
}

function createAtomicModel(element) {
    const nucleusGeometry = new THREE.SphereGeometry(0.5, 32, 32);
    const nucleusMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const nucleus = new THREE.Mesh(nucleusGeometry, nucleusMaterial);
    scene.add(nucleus);

    element.quantum_states.forEach((state, index) => {
        const electronGeometry = new THREE.SphereGeometry(0.1, 32, 32);
        const electronMaterial = new THREE.MeshBasicMaterial({ color: 0x0000ff });
        const electron = new THREE.Mesh(electronGeometry, electronMaterial);

        const radius = 1 + state[0] * 0.5;
        const angle = (index / element.quantum_states.length) * Math.PI * 2;
        electron.position.set(Math.cos(angle) * radius, Math.sin(angle) * radius, 0);
        scene.add(electron);
    });
}

function displayElementData(data) {
    elementDetails.innerHTML = `
        <h2>${data.name} (${data.symbol})</h2>
        <p>Ground State: ${data.ground_state}</p>
        <p>Excited States: ${data.excited_states.join(', ')}</p>
        <p>Properties: Atomic Mass = ${data.properties.atomic_mass}, Density = ${data.properties.density}</p>
        <p>Electronic Configuration: ${data.ground_state}</p>
    `;
    while (scene.children.length > 0) {
        scene.remove(scene.children[0]);
    }
    createAtomicModel(data);
    createBlochSphere();
}

function saveVisualization(filename) {
    renderer.render(scene, camera);
    const imgData = renderer.domElement.toDataURL('image/png');
    const link = document.createElement('a');
    link.href = imgData;
    link.download = filename;
    link.click();
}

function searchElement(query) {
    const results = Object.values(ELEMENT_DATA).filter(element =>
        element.name.toLowerCase().includes(query.toLowerCase()) || element.symbol.toLowerCase() === query.toLowerCase()
    );
    return results;
}

document.addEventListener('DOMContentLoaded', () => {
    elementDetails = document.getElementById('elementDetails');

    document.getElementById('fetchElement').addEventListener('click', () => {
        const atomicNumber = document.getElementById('atomicNumberInput').value;
        if (atomicNumber) {
            fetchElementData(atomicNumber);
        } else {
            alert('Please enter a valid atomic number.');
        }
    });

    document.getElementById('periodicTable').addEventListener('click', (event) => {
        const atomicNumber = prompt("Enter the atomic number you clicked on:");
        if (atomicNumber) {
            fetchElementData(atomicNumber);
        }
    });

    document.getElementById('info').innerHTML += '<button id="saveVisualization">Save Visualization</button>';
    document.getElementById('saveVisualization').addEventListener('click', () => {
        saveVisualization('visualization.png');
    });

    document.getElementById('info').innerHTML += '<input type="text" id="searchInput" placeholder="Search Element">';
    document.getElementById('searchInput').addEventListener('input', (event) => {
        const query = event.target.value;
        const results = searchElement(query);
        if (results.length > 0) {
            displayElementData(results[0]);
        }
    });

    init();
});
}