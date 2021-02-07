const searchPokemon=async () => {
    npokemon = document.getElementById("npokemon")
    console.log('npokemon',npokemon)
    const response = await fetch('http://localhost:5000/?id='+npokemon.value);
    console.log(response)
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson)
    a=JSON.stringify(myJson)
    obj=JSON.parse(a)
    arr=Object.values(obj)
    var cambiar;
    var imgcambiar;
    muestra= myJson;
    document.getElementById("imgchange").src=obj.imagen
    cambiar=document.getElementById("cambiar");
    cambiar.innerHTML=arr[1];
    document.body.style.backgroundColor='#A1CDE5';
    

}

