document.addEventListener('DOMContentLoaded', function() {
    let calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        events: '/api/get_events/',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        dateClick: function(info) {
            document.getElementById('start_date').value = info.dateStr;
            document.getElementById('end_date').value = info.dateStr;
            clearForm();
        },
        eventClick: function(info) {
            const event = info.event;
            document.getElementById('event-id').value = event.id;
            document.getElementById('title').value = event.title;
            document.getElementById('task_type').value = event.extendedProps.task_type;
            document.getElementById('crop').value = event.extendedProps.crop_id;
            document.getElementById('start_date').value = event.startStr;
            document.getElementById('end_date').value = event.endStr;
        }
    });
    calendar.render();
});


function fetchUserLocationAndWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;

                // Adjust fetch URL
                fetch(`/calendar/api/get_weather/?lat=${latitude}&lon=${longitude}`)
                    .then(response => response.json())
                    .then(data => {
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
                    .catch(error => console.error('Erro ao obter clima:', error));
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


function saveEvent() {
    // Determine if adding or editing an event based on presence of event ID
    const eventId = document.getElementById('event-id').value;
    const url = eventId ? `/api/edit_event/${eventId}/` : '/api/add_event/';
    
    // Collect event data from form fields
    const eventData = {
        title: document.getElementById('title').value,
        task_type: document.getElementById('task_type').value,
        crop_id: document.getElementById('crop').value,
        start_date: document.getElementById('start_date').value,
        end_date: document.getElementById('end_date').value,
    };

    // Get CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
    if (!csrfToken) {
        console.error("CSRF token not found.");
        return;
    }

    // Perform the save (add/edit) action
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(eventData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(eventId ? 'Evento atualizado com sucesso!' : 'Evento adicionado com sucesso!');
            clearForm();
            location.reload();  // Reload the page to see updated events
        } else {
            alert('Erro ao salvar o evento.');
        }
    })
    .catch(error => console.error('Erro ao salvar evento:', error));
}

function clearForm() {
    // Clear the event form fields
    document.getElementById('event-form').reset();
    document.getElementById('event-id').value = '';
}
