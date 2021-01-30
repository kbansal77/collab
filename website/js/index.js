  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {
      constrainWidth:false,
      alignment: "right",
      coverTrigger: false
    });

    var elems = document.querySelectorAll('.tabs');
    var instance = M.Tabs.init(elems, {
      swipeable: true
    });

  });