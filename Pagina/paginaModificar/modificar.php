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

// Obtener los valores ingresados por el usuario
$id = $_POST['id'];
$entry = $_POST['entry'];
$reviewed = $_POST['reviewed'];
$entry_name = $_POST['entry_name'];
$protein_name = $_POST['protein_names'];
$gene_names = $_POST['gene_names'];
$organism = $_POST['organism'];
$Length = $_POST['Length'];

// Consulta para actualizar el registro
$sql = "UPDATE tomate SET entry = '$entry', reviewed = '$reviewed', entry_name = '$entry_name', protein_names = '$protein_name', gene_names = '$gene_names', organism = '$organism', Length = '$Length' WHERE Id = $id";

if ($conn->query($sql) === TRUE) {
    echo "Registro modificado exitosamente.";
} else {
    echo "Error al modificar el registro: " . $conn->error;
}

$conn->close();
?>