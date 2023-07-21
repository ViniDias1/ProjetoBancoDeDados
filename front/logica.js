$(document).ready(function() {
  carregarUsuarios();

  $('#btnCadastrar').click(function() {
    cadastrarUsuario();
  });

  $('#btnPesquisar').click(function() {
    pesquisarUsuarioPorCPF(parseInt($('#cpfPesquisa').val()));
  });
});

function exibirUsuarios(data,diff) {

  if (diff == 1){

    let userCPF = $('#userCPF');
    userCPF.empty();
    userCPF.append('CPF: ' + data.cpf + ' - Nome: ' + data.nome + ' - Data de Nascimento: ' + data.data_nascimento);
    return;
  }
  let userList = $('#userList');
  userList.empty();
  
  for (dados in data){
    dados = data[dados]
    let li = $('<li>').text('CPF: ' + dados.cpf + ' - Nome: ' + dados.nome + ' - Data de Nascimento: ' + dados.data_nascimento);
    userList.append(li);
  }

}

function limparCampos() {
  $('#nome').val('');
  $('#cpf').val('');
  $('#dataNascimento').val('');
}

function carregarUsuarios() {
  $.get("http://localhost:5000/allUsers", function(data) {
    exibirUsuarios(data,0);
  });
}

function pesquisarUsuarioPorCPF(cpf) {
  $.get("http://localhost:5000/user/" + cpf, function(data) {
    exibirUsuarios(data,1);
  });
}

function cadastrarUsuario() {
  let nome = $('#nome').val();
  let cpf = parseInt($('#cpf').val());
  let dataNascimento = $('#dataNascimento').val();

  let novoUsuario = {
    "cpf": cpf,
    "nome": nome,
    "data_nascimento": dataNascimento
  };

  $.ajax({
    type: "POST",
    url: "http://localhost:5000/addUser",
    data: JSON.stringify(novoUsuario),
    contentType: "application/json",
    success: function(response) {
      alert("Usuário cadastrado com sucesso!");
      carregarUsuarios();
      limparCampos();
    },
    error: function(error) {
      alert("Erro ao cadastrar usuário. Por favor, tente novamente.");
    }
  });
}
