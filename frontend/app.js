$(document).ready(function() {
    // Toggle sidebar
    $('#sidebar-toggle').click(function() {
        $('.ui.sidebar').sidebar('toggle');
    });

    // Fetch and display data
    function fetchData() {
        // This is a placeholder. You'll need to implement actual data fetching from your server.
        const mockData = [
            { title: 'Session 1', description: 'Description for Session 1', type: 'Breakout Session', topic: 'AI/ML' },
            { title: 'Session 2', description: 'Description for Session 2', type: 'Workshop', topic: 'Serverless' },
            // Add more mock data as needed
        ];

        displayData(mockData);
    }

    function displayData(data) {
        const content = $('#content');
        content.empty();

        data.forEach(item => {
            const card = `
                <div class="card">
                    <div class="content">
                        <div class="header">${item.title}</div>
                        <div class="meta">${item.type} | ${item.topic}</div>
                        <div class="description">${item.description}</div>
                    </div>
                </div>
            `;
            content.append(card);
        });
    }

    fetchData();
});
