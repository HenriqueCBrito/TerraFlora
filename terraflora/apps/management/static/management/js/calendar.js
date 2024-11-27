document.addEventListener('DOMContentLoaded', function () {
    let calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        events: '/api/get_events/',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay',
        },
        dateClick: function (info) {
            document.getElementById('start_date').value = info.dateStr;
            document.getElementById('end_date').value = info.dateStr;
            clearForm();
        },
        eventClick: function (info) {
            const event = info.event;
            document.getElementById('event-id').value = event.id;
            document.getElementById('title').value = event.title;
            document.getElementById('task_type').value = event.extendedProps.task_type;
            document.getElementById('crop').value = event.extendedProps.crop_id;
            document.getElementById('start_date').value = event.startStr;
            document.getElementById('end_date').value = event.endStr;
            document.getElementById('description').value = event.extendedProps.description || '';
            document.getElementById('priority').value = event.extendedProps.priority || 'Medium';
        },
        eventRender: function (info) {
            if (info.event.extendedProps.priority === 'High') {
                info.el.style.backgroundColor = 'red';
            } else if (info.event.extendedProps.priority === 'Medium') {
                info.el.style.backgroundColor = 'orange';
            } else {
                info.el.style.backgroundColor = 'green';
            }
        },
    });
    calendar.render();
});

function fetchUserLocationAndWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                fetch(`/calendar/api/get_weather/?lat=${latitude}&lon=${longitude}`)
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.error) {
                            document.getElementById('weather-widget').innerHTML = "Erro ao obter dados meteorológicos.";
                        } else {
                            document.getElementById('weather-widget').innerHTML = `
                                <p>${data.location.name}, ${data.location.region}</p>
                                <p>${data.current.temp_c}°C - ${data.current.condition}</p>
                                <p>Vento: ${data.current.wind_kph} km/h | Umidade: ${data.current.humidity}%</p>
                            `;
                        }
                    })
                    .catch((error) => console.error('Erro ao obter clima:', error));
            },
            (error) => {
                console.error('Erro ao obter localização:', error);
                document.getElementById('weather-widget').innerHTML = "Localização não permitida.";
            }
        );
    } else {
        console.error('Geolocalização não é suportada pelo navegador.');
        document.getElementById('weather-widget').innerHTML = "Geolocalização não suportada pelo navegador.";
    }
}

function validateForm(eventData) {
    if (
        !eventData.title ||
        !eventData.task_type ||
        !eventData.crop_id ||
        !eventData.start_date ||
        !eventData.end_date
    ) {
        alert("Todos os campos obrigatórios devem ser preenchidos.");
        return false;
    }
    return true;
}

function saveEvent() {
    const eventId = document.getElementById('event-id').value;
    const url = eventId ? `/api/edit_event/${eventId}/` : '/api/add_event/';

    const eventData = {
        title: document.getElementById('title').value,
        task_type: document.getElementById('task_type').value,
        crop_id: document.getElementById('crop').value,
        start_date: document.getElementById('start_date').value,
        end_date: document.getElementById('end_date').value,
        description: document.getElementById('description').value,
        priority: document.getElementById('priority').value,
    };

    if (!validateForm(eventData)) {
        return;
    }

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    if (!csrfToken) {
        console.error("CSRF token not found.");
        return;
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(eventData),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status === 'success') {
                alert(eventId ? 'Evento atualizado com sucesso!' : 'Evento adicionado com sucesso!');
                clearForm();
                location.reload();
            } else {
                alert('Erro ao salvar o evento.');
            }
        })
        .catch((error) => console.error('Erro ao salvar evento:', error));
}

function clearForm() {
    document.getElementById('event-form').reset();
    document.getElementById('event-id').value = '';
}
