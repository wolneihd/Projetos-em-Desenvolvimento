var body = document.getElementById('body');

async function fetchData(){
	try {
		var cidade = document.getElementById('cidade').value;
		var uf = document.getElementById('uf').value;
		var logradouro = document.getElementById('logradouro').value;
		
		const response = await fetch(`https://viacep.com.br/ws/${uf}/${cidade}/${logradouro}/json/`);
		if (!response.ok) {
			throw new error ("Could not fetch resource!");
		}
		const data = await response.json();
		console.log(data);
		
		function getTH() {
			var tabela = document.getElementById('table');
			tabela.className = 'tabela';
			const column = ['id','CEP', 'Logradouro', 'Complemento', 'Bairro', 'Localidade', 'UF'];
			const head = document.querySelector('thead');
			let tags = '<tr>';
			for (i=0;i<column.length;i++) {
				tags += `<th>${column[i]}</th>`;
			}
			tags += '</tr>';
			head.innerHTML = tags;
			getTD();
		}
		function getTD() {
			const tbody = document.querySelector('tbody');
			let tags = '';
			console.log(data.length);
			for (i=0;i<data.length;i++) {
				tags += `<tr>
					<td>${i+1}</td>
					<td>${data[i].cep}</td>
					<td>${data[i].logradouro}</td>
					<td>${data[i].complemento}</td>
					<td>${data[i].bairro}</td>
					<td>${data[i].localidade}</td>
					<td>${data[i].uf}</td>
				</tr>` 	
			}			
			tbody.innerHTML = tags;
		}
		
		getTH();
	}
	
	catch(error){
		console.error(error);
	}
}