$(document).ready(function() {
    // Inicialize o DataTables
    $('#patrimonioTable').DataTable({
        // Configurações adicionais do DataTables, se necessário
        ajax: {
            url: '/listagem', // URL da rota que retorna os dados
            type: 'GET',
            beforeSend: function(xhr) {
                const token = localStorage.getItem('access_token');
                if (token) {
                    xhr.setRequestHeader('Authorization', 'Bearer ' + token);
                }
            },
            dataSrc: ''
        },
        columns: [
            { data: 'id' },
            { data: 'nome' },
            { data: 'categoria' },
            { data: 'status' },
            {
                data: null,
                render: function(data, type, row) {
                    return `
                        <a href="/editar/${row.id}" class="btn btn-warning" data-toggle="modal" data-target="#editarModal" data-id="${row.id}" data-nome="${row.nome}" data-categoria="${row.categoria}" data-status="${row.status}">Editar</a>
                        <form method="POST" action="/apagar/${row.id}" style="display:inline;">
                            <button type="submit" class="btn btn-danger">Apagar</button>
                        </form>
                    `;
                }
            }
        ]
    });

    // Preencher a modal de edição com os dados do patrimônio selecionado
    $('#editarModal').on('show.bs.modal', function(event) {
        const button = $(event.relatedTarget); // Botão que acionou a modal
        const id = button.data('id');
        const nome = button.data('nome');
        const categoria = button.data('categoria');
        const status = button.data('status');

        const modal = $(this);
        modal.find('#editarNome').val(nome);
        modal.find('#editarCategoria').val(categoria);
        modal.find('#editarStatus').val(status);

        // Atualizar a ação do formulário com o ID correto
        const form = modal.find('#editarForm');
        form.attr('action', `/editar/${id}`);
    });
});