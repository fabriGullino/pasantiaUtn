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

// Obtener el valor del ID ingresado por el usuario
$id = $_POST['id'];

// Consulta para eliminar el registro
$sql = "DELETE FROM tomate WHERE Id = $id";

if ($conn->query($sql) === TRUE) {
    echo "Registro eliminado exitosamente.";
} else {
    echo "Error al eliminar el registro: " . $conn->error;
}

$conn->close();
?>
