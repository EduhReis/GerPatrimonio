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
                        <a href="/editar/${row.id}" class="btn btn-warning">Editar</a>
                        <form method="POST" action="/apagar/${row.id}" style="display:inline;">
                            <button type="submit" class="btn btn-danger">Apagar</button>
                        </form>
                    `;
                }
            }
        ]
    });
});