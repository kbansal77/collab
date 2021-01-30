  document.addEventListener('DOMContentLoaded', function() {
    var date = new Date()
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, {
      constrainWidth:false,
      alignment: "right",
      coverTrigger: false
    });

    var chip_elems = document.querySelectorAll('.chips');
    var instances = M.Chips.init(chip_elems, {
      placeholder:"Enter Tech Stack",
      secondaryPlaceholder:"Enter Tech Stack"
    });

    var date_elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(date_elems, {
      minDate: date,
      autoClose: true,
      yearRange:0
    });

  });
  // ember773