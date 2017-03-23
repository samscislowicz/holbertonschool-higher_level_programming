//fetches and replaces the name of this URL: http://swapi.co/api/people/5/?format=json
$.get('http://swapi.co/api/people/5/?format=json' function (body) {
  $('DIV#character').text(body.name);
});
