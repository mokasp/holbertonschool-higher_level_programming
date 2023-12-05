$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
    $(data.results).each(function(index, value) {
        $('#list_movies').append(`<li>${value.title}</li>`)
    })})
