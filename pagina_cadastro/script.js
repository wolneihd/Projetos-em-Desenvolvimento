function validar_nome() {
	var nome = document.getElementById('entry_nome').value;
	var tamanho_nome = nome.length;
	if (tamanho_nome == 0) {
		alert('O campo nome não está preenchido. Favor preencher!');
	}
	else if (tamanho_nome > 40) {
		alert('O campo nome tem mais de 40 carateres. Nome deve ser reduzido até 40!');
	}
	else {
		return nome;
	}
}

function validar_idade() {
	var idade = document.getElementById('entry_idade').value;
	if (idade <= 0) {
		alert('Idade inválida ou campo vazio. Favor verificar!')
	}
	else {
		return idade;
	}
}

function validar_cpf() {	
	var cpf = document.getElementById('entry_cpf').value;
	if (cpf.length != '') {
		var cpf_limpo = '';
		var tamanho_cpf = cpf.length;
		for (i=0;i<tamanho_cpf;i++) {
			if (cpf[i] == '.') {
				cpf_limpo = cpf_limpo + '';
			}
			else if (cpf[i] == '-') {
				cpf_limpo = cpf_limpo + '';
			}
			else if (cpf[i] == '/') {
				cpf_limpo = cpf_limpo + '';
			}
			else {
				cpf_limpo = cpf_limpo + cpf[i];
			}
		}
		if (cpf_limpo.length == 11) {
			var contador = 10;
			var somador = 0;
			var digito_01;
			var digito_02;
			for (i=0;i<9;i++) {
				somador = somador + (cpf_limpo[i]*contador);
				//console.log(cpf_limpo[i],contador,somador);
				contador--;
			}
			digito_01 = (somador % 11);
			if (digito_01 == 1) {
				digito_01 = 0;
			}
			else {
				digito_01 = 11-digito_01;
			}
			var contador = 11;
			var somador = 0;			
			for (i=0;i<10;i++) {
				somador = somador + (cpf_limpo[i]*contador);
				//console.log(cpf_limpo[i],contador,somador);
				contador--;
			}
			digito_02 = (somador % 11);
			if (digito_02 == 1) {
				digito_02 = 0;
			}
			else {
				digito_02 = 11-digito_02;
			}
			if (digito_01 == cpf_limpo[9] && digito_02 == cpf_limpo[10]) {
				return cpf_limpo;
			}
			else {
				alert('O CPF informado é inválido!');
			}
		}
		else
		{
			alert('A quantidade de caracteres no CPF diverge. Favor verificar!')
		}
	}
	else {
		alert('Campo CPF está vazio. Favor verificar!')
	}
	
}

function mensagem_sucesso() {
	var qtd_msg_sucesso = document.getElementsByClassName('texto_sucesso');
	if (qtd_msg_sucesso.length == 0) {
		var mensagem = document.createElement('p');
		var texto = document.createTextNode("Dados gerados com sucesso!");
		mensagem.className = 'texto_sucesso';
		mensagem.appendChild(texto);
		document.body.appendChild(mensagem);	
	}
}

function mensagem_erro() {
	var qtd_msg_erro = document.getElementsByClassName('texto_erro');
	if (qtd_msg_erro.length == 0) {
		var mensagem_erro = document.createElement('p');
		var texto_erro = document.createTextNode("Dados inválidos. Favor verificar!");
		mensagem_erro.className = 'texto_erro';
		mensagem_erro.appendChild(texto_erro);
		document.body.appendChild(mensagem_erro);	
	}
}



function salvar() {
	if (validar_nome()!= undefined && validar_idade()!= undefined && validar_cpf()!= undefined) {
		const dados_salvos = {nome: validar_nome(), idade: validar_idade(), cpf: validar_cpf()}; 
		mensagem_sucesso();	
		console.log(dados_salvos);
	}
	else {
		mensagem_erro();
		console.log('Algum dado incorreto. Usuário deve preencher corretamente.')		
	}
}

function limpar() {
	document.getElementById('entry_nome').value = '';
	document.getElementById('entry_idade').value = '';
	document.getElementById('entry_cpf').value = '';
}
