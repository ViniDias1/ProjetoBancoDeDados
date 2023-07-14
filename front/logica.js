$(document).ready(function() {
  carregarUsuarios();

  $('#btnCadastrar').click(function() {
    cadastrarUsuario();
  });
});

function exibirUsuarios(data) {
  let userList = $('#userList');
  userList.empty();

  data.forEach(function(usuario) {
    let li = $('<li>').text('CPF: ' + usuario.cpf + ' - Nome: ' + usuario.nome + ' - Data de Nascimento: ' + usuario.data_nascimento);
    userList.append(li);
  });
}

function limparCampos() {
  $('#nome').val('');
  $('#cpf').val('');
  $('#dataNascimento').val('');
}

function carregarUsuarios() {
  $.get("http://localhost:5000/allUsers", function(data) {
    exibirUsuarios(data);
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

