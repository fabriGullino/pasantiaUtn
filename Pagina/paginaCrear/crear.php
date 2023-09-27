<?php
// Conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "gramene";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}

$entry = $_POST['entry'];
$reviewed = $_POST['reviewed'];
$entry_name = $_POST['entry_name'];
$protein_name = $_POST['protein_names'];
$gene_names = $_POST['gene_names'];
$organism = $_POST['organism'];
$Length = $_POST['Length'];

// Consulta para insertar el nuevo registro
$sql = "INSERT INTO tomate (entry, reviewed, entry_name, protein_names, gene_names, organism, Length) VALUES ('$entry', '$reviewed', '$entry_name', '$protein_name', '$gene_names', '$organism', '$Length')";

if ($conn->query($sql) === TRUE) {
    echo "Nuevo registro creado exitosamente.";
} else {
    echo "Error al crear el registro: " . $conn->error;
}

$conn->close();
?>