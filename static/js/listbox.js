$(".draggable-left, .draggable-right").sortable({
    connectWith: ".connected-sortable",
    stack: ".connected-sortable ul"
    }).disableSelection();