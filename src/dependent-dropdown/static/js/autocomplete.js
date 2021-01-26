$(function() {
    var persons = [
      'python',
      'java',
      'html',
      'css'
    ];
    $("#personName").autocomplete({
      source: "{% url 'autocomplete' %}",
    });
  } );