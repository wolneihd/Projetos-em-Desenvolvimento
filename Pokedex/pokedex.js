async function fetchData(){
	try {
		const pokemonName = document.getElementById("pokemonName").value.toLowerCase();
		
		const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
		if (!response.ok) {
			throw new error ("Could not fetch resource!");
		}
		const data = await response.json();
		console.log(data);
		
		//const pokemonSprite = data.sprites.front_default;
		const pokemonSprite = data.sprites.other.home.front_default;
		const imgElement = document.getElementById('pokemonSprite');
		imgElement.src = pokemonSprite;
		imgElement.style.display = 'block';
		
		const nomePokemon = data.name;
		const tagNome = document.getElementById('nomePok').innerHTML = nomePokemon;
		
		const tipoPokemon = data.types[0].type.name;
		const tagTipo = document.getElementById('tipoPok').innerHTML = tipoPokemon;
		
	}
	
	catch(error){
		console.error(error);
	}
}

async function fetchNumero(){
	try {
		const pokemonNumero = document.getElementById("pokemonId").value;
		
		const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonNumero}`);
		if (!response.ok) {
			throw new error ("Could not fetch resource!");
		}
		const data = await response.json();
		console.log(data);
		
		//const pokemonSprite = data.sprites.front_default;
		const pokemonSprite = data.sprites.other.home.front_default;
		const imgElement = document.getElementById('pokemonSprite');
		imgElement.src = pokemonSprite;
		imgElement.style.display = 'block';
		
		const nomePokemon = data.name;
		const tagNome = document.getElementById('nomePok').innerHTML = nomePokemon;
		
		const tipoPokemon = data.types[0].type.name;
		const tagTipo = document.getElementById('tipoPok').innerHTML = tipoPokemon;
		
	}
	
	catch(error){
		console.error(error);
	}
}