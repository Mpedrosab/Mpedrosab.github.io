<?php
echo "HOLA";
if(isset($_GET["query"])){
echo "HOLA";


try {
$bd = new PDO('sqlite:../../Data/ParamDB.db');

   // $_POST["query"]='SELECT * FROM Params';
    
   // $queryText='SELECT + FROM Params';
$resultado = $bd->query($_POST["query"]);
    $arrayAll=[];
    
     foreach ($resultado as $row) {
    // while ($row = $resultado->fetch_assoc()) {
     array_push($arrayAll, $row);


    }
    
          //  echo $_POST["query"].json_encode($resultado). "\n";
            echo json_encode($arrayAll);
//echo json_encode($resultado);
}
    catch (PDOException $e) {
      // this is rolback fanction
      //$bd->rollback();
      echo "query is not exe: ".$e;
    }
}
    
    ?>