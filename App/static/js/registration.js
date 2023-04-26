
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

function submitInvitedForm(e) {
  console.log(ksa_visa)
  e.preventDefault()

  var ksa_visa=$('input[name=ksa-visa]:checked', '#invated-reg-form').val()
  
  var m_form=new FormData($('#invated-reg-form')[0])
  m_form.append('ksa-visa',ksa_visa)
  m_form.append('csrfmiddlewaretoken',csrftoken)

  $.ajax({
      type: "POST",
      url: "submitInvitedform",
      data: m_form,
      processData: false,
      contentType: false,
      dataType: "json",
      success: function (res) {

        fetch('send_invited_reg_success_mail',{method: "POST", headers: {'X-CSRFToken': csrftoken,'Content-Type':'application/json'},
        body:JSON.stringify({'reg_id':res.reg_id})})

          Swal.fire({
              position: 'top-center',
              icon: 'success',
              title: 'Your registration has been submited',
              showConfirmButton: false,
              timer: 1500

            })

            setTimeout(() => {
              $('#invated-reg-form')[0].reset()
              window.location.href=window.location.origin

            }, 2000);
          
      }
  });
  
}

function submitApplicantForm(e) {

  e.preventDefault()
  var m_form=new FormData($('#applicant-reg-form')[0])
  m_form.append('csrfmiddlewaretoken',csrftoken)

  var intrested_list=[]
  $("input:checkbox[name=type]:checked").each(function(){
    intrested_list.push($(this).val());
  });

  inspectForm(m_form)
  $.ajax({
      type: "POST",
      url: "submitApplicantform",
      data: m_form,
      processData: false,
      contentType: false,
      dataType: "json",
      success: function (res) {

        // fetch('send_applicant_reg_success_mail',{method: "POST", headers: {'X-CSRFToken': csrftoken,'Content-Type':'application/json'},
        // body:JSON.stringify({'reg_id':res.reg_id})})
        send_mail('send_applicant_reg_success_mail',res.reg_id)
        
          Swal.fire({
              position: 'top-center',
              icon: 'success',
              title: 'Your registration has been submited',
              showConfirmButton: false,
              timer: 1500

            })

            setTimeout(() => {
              $('#applicant-reg-form')[0].reset()
              window.location.href=window.location.origin

            }, 2000);
          
      }
  });

}

//debug purpose only not use in production 
function inspectForm(m_form) {
  
  for (const [key, value] of m_form.entries()) {
    console.log(key,'=',value);
  }

}

function send_mail(url,reg_id) {
  $.ajax({
    type: "POST",
    url: url,
    data: {reg_id:reg_id,'csrfmiddlewaretoken':csrftoken},
    dataType: "json",
    success: function (response) {
      
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