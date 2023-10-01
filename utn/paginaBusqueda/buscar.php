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

$campo = $_POST['opcion'];

// Obtener la búsqueda ingresada por el usuario
$busqueda = $_POST['busqueda'];

// Divide la entrada en un array de términos de búsqueda
$terminos = explode(",", $busqueda);

// Limpia y escapa cada término de búsqueda
$terminosLimpios = array_map(function($term) use ($conn) {
    return trim(mysqli_real_escape_string($conn, $term));
}, $terminos);

// Consulta a la base de datos
$sql = "SELECT * FROM tomate WHERE $campo LIKE '%" . implode("%' OR $campo LIKE '%", $terminosLimpios) . "%'";
$result = $conn->query($sql);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UTN</title>

    <link rel="stylesheet" href="../css/estilos.css">

    <script src="https://kit.fontawesome.com/41bcea2ae3.js" crossorigin="anonymous"></script>
</head>
<body id="body">
    
    <header>
        <div class="icon__menu">
            <i class="fas fa-bars" id="btn_open"></i>
        </div>
    </header>

    <div class="menu__side" id="menu_side">

        <div class="name__page">
            <img src="../assets/UTN_logo-removebg-preview.ico" class="icon__UTN"></img>
            <a class="name__menu">Menu</a>
        </div>

        <div class="options__menu">	
            
            <ul class="list">

                <li class="list__item">
                    <div class="list__button">
                        <img src="../assets/home.svg" class="list__img">
                        <a href="#inicio" class="nav__link">Inicio</a>
                    </div>
                </li>
    
                <li class="list__item list__item--click">
                    <div class="list__button list__button--click">
                        <img src="../assets/herramientas.svg" class="list__img" id="btn_open">
                        <a href="#" class="nav__link">Herramientas</a>
                        <img src="../assets/arrow.svg" class="list__arrow">
                    </div>
    
                    <ul class="list__show">
                        <li class="list__inside">
                            <a href="#busca" class="nav__link nav__link--inside">Buscar<img src="../assets/busca.svg" class="list__img2"></a>
                            
                        </li>
                    </ul>
    
                </li>
    
                <li class="list__item">
                    <div class="list__button">
                        <img src="../assets/lista.svg" class="list__img">
                        <a href="#carrito" class="nav__link">Mi investigacion</a>
                    </div>
                </li>
    
                <li class="list__item">
                    <div class="list__button">
                        <img src="../assets/message.svg" class="list__img">
                        <a href="#contacto" class="nav__link">Contacto</a>
                    </div>
                </li>
    
            </ul>
        </div>
    </div>

    <main>
        <!--Introduccion-->
        <div class="container" >
            <div class="logo">
                <img src="../assets/UTN_logo-removebg-preview.png" id="inicio">
            </div>
        <h1>--Introduccion--</h1><br>
        <p>Esta pagina de codigo libre esta diseñada para tareas/trabajos de...</p> <br>
        <p>(Tutorial basico sobre el uso de la pagina)</p>
        </div>

        <br>
        <br>
        <br>
        <br>
        <br>

        <!--Buscador-->
            <div class="container">
                <div class="logo">
                    <img src="../assets/UTN_logo-removebg-preview.png" id="busca">
                </div>
                <h1>UTN data search</h1>
                <div class="tools-container">
                    <form id="product-form">
                        <select id="frutas" name="opcion">
                            <option value="BuscarPor">Buscar por...</option>
                            <option value="Id">Id</option>
                            <option value="entry_name">Entry Name</option>
                            <option value="entry">Entry</option>
                            <option value="gene_names">Gene Name</option>
                            <option value="organism">Organism</option>
                            <option value="protein_names">Protein Name</option>
                        </select>
                        <input type="text" name="busqueda" placeholder="Ingresa tu búsqueda" id="searchInput">
                        <button type="submit" id="searchButton" value="Buscar">Buscar</button>
                    </form>
                </div>
                <table id="resultsTable">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Entry</th>
                            <th>Reviewed</th>
                            <th>Entry Name</th>
                            <th>Protein Name</th>
                            <th>Gene Name</th>
                            <th>Organism</th>
                            <th>Length</th>
                        </tr>
                    </thead>
                    <tbody>
                    <?php
                    if ($result->num_rows > 0) {
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
                    ?>
                    </tbody>
                </table>
            </div>
    </main>
    <script src="../js/script.js"></script>
</body>
</html>