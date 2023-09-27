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

// Obtener la búsqueda ingresada por el usuario
$busqueda44 = $_POST['busqueda4'];

// Divide la entrada en un array de términos de búsqueda
$terminos = explode(",", $busqueda44);

// Inicializa un array para almacenar las condiciones de búsqueda
$condiciones = [];

foreach ($terminos as $termino) {
    // Limpia y escapa cada término de búsqueda
    $termino = trim(mysqli_real_escape_string($conn, $termino));
    
    // Agrega la condición a la lista de condiciones
    $condiciones[] = "gene_names LIKE '%$termino%'";
}

// Construye la consulta SQL con condiciones OR
$sql = "SELECT * FROM tomate WHERE " . implode(" OR ", $condiciones);

$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados de la búsqueda</title>
    <link rel="stylesheet" href="../pasantia/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
</head>
<body>
<table>
    <?php
    if ($result->num_rows > 0) {
        echo "<ul>";
        echo "<td>ID</td>";
        echo "<td>Entry</td>";
        echo "<td>Reviewed</td>";
        echo "<td>Entry Name</td>";
        echo "<td>Protein Names</td>";
        echo "<td>Gene Names</td>";
        echo "<td>Organism</td>";
        echo "<td>Length</td>";
        echo "</ul>";
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row['Id'] . "</td>";
            echo "<td>" . $row['entry'] . "</td>";
            echo "<td>" . $row['reviewed'] . "</td>";
            echo "<td>" . $row['entry_name'] . "</td>";
            echo "<td>" . $row['protein_names'] . "</td>";
            echo "<td>" . $row['gene_names'] . "</td>";
            echo "<td>" . $row['organism'] . "</td>";
            echo "<td>" . $row['Length'] . "</td>";
            echo "</tr>";
        }
    } else {
        echo "No se encontraron resultados";
    }
    $conn->close();
    ?>
</table>
</body>
</html>
