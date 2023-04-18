
function submitSpeakerForm(e) {
   
    e.preventDefault()

    var ksa_visa=$('input[name=ksa-visa]:checked', '#speaker-reg-form').val()
    console.log(ksa_visa)
    var m_form=new FormData($('#speaker-reg-form')[0])
    m_form.append('ksa-visa',ksa_visa)
    m_form.append('csrfmiddlewaretoken',csrftoken)

    $.ajax({
        type: "POST",
        url: "submitspeakerform",
        data: m_form,
        processData: false,
        contentType: false,
        dataType: "json",
        success: function (res) {

          fetch('send_speaker_reg_success_mail',{method: "POST", headers: {'X-CSRFToken': csrftoken,'Content-Type':'application/json'},
          body:JSON.stringify({'reg_id':res.reg_id})})

            Swal.fire({
                position: 'top-center',
                icon: 'success',
                title: 'Your registration has been submited',
                showConfirmButton: false,
                timer: 1500

              })

              setTimeout(() => {
                $('#speaker-reg-form')[0].reset()
                window.location.href=window.location.origin

              }, 2000);
            
        }
    });
    
}


/// extras

$(document).ready(function () {
  $("#country").select2({
    placeholder: "Select a country",
  templateResult: formatCountry,
    data: isoCountries,
    theme:'bootstrap-5',
    
   
  })

 
  
});


function formatCountry (country) {
  if (!country.id) { return country.text; }
  var country = $(
    '<span class="flag-icon flag-icon-'+ country.iso.toLowerCase() +' flag-icon-squared"></span>' +
    '<span class="flag-text">'+ country.text+"</span>"
  );
  return country;
};


// slide up and down

$(document).ready(function() {
  if ($('#attendyes').prop('checked')) {
    $('#previous-forum').slideDown();
  }
  
  $('#attendyes').click(function() {
    $('#previous-forum').slideDown();
  });
  
  $('#attendno').click(function() {
    $('#previous-forum').slideUp();
  });
});