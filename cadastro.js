document.getElementById('empresaForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const senha = document.getElementById('senha').value;
    const confirmarSenha = document.getElementById('confirmarSenha').value;

    if (senha !== confirmarSenha) {
        alert('As senhas não coincidem!');
    } else {
        alert('Cadastro realizado com sucesso!');
    }
});