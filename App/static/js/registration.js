
function submitSpeakerForm(e) {
   
    e.preventDefault()

    if ($('#speaker-reg-form input[type="file"].file-size-over').length > 0){
      $('input[type="file"]').focus()
      return false;
    }

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
            text: 'Thank you for registering your interest to attend Next World Forum. Please expect to receive an email from the Next World team',
            showConfirmButton: true,


          })

              setTimeout(() => {
                $('#speaker-reg-form')[0].reset()
                // window.location.href=window.location.origin

              }, 2000);
            
        }
    });
    
}

async function submitInvitedForm(e) {
  e.preventDefault()
  var valid=false
  var code_message=''
  await check_code_is_valid($('#code-inp').val()).then(res => {

    valid=res.valid
    code_message=res.reason
    
  }
 )

  if (!valid){

   // $('#code-inp').focus()
   
    $('#code-message').html(code_message)
    $('.unique-code-div').show()
    $('.main-div').hide()
    return false

  }
  else{
  
  $('#code-message').html('')
  
  if ($('#invated-reg-form input[type="file"].file-size-over').length > 0){
    $('input[type="file"]').focus()
    return false;
  }

  var ksa_visa=$('input[name=ksa-visa]:checked', '#invated-reg-form').val()
  
  var m_form=new FormData($('#invated-reg-form')[0])
  m_form.append('ksa-visa',ksa_visa)
  m_form.append('csrfmiddlewaretoken',csrftoken)

  var intrested_list=[]
  $("input:checkbox[name='Interested']:checked").each(function(){
    intrested_list.push($(this).val());
  });

  m_form.append('intrested_in',JSON.stringify(intrested_list))
  m_form.append('urc-code',$('#code-inp').val())
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
          text: 'Thank you for registering your interest to attend Next World Forum. Please expect to receive an email from the Next World team',
          showConfirmButton: true,


        })

            setTimeout(() => {
              $('#invated-reg-form')[0].reset()
              // window.location.href=window.location.origin

            }, 2000);
          
      }
  });

}

}


function validate_form(form_id) {

  
  var invalidInputs = $('#'+form_id+' :input').filter(function() {
    return !this.checkValidity();
  }).each(function() {

  this.addEventListener("input", function(){
 
   if (!this.checkValidity()){
    $('#'+this.id+'-error').removeClass('d-none')
   }
   else{
    $('#'+this.id+'-error').addClass('d-none')
   }
   

  });
    $('#'+this.id+'-error').removeClass('d-none')
   
  })

}

 function submitApplicantForm(e) {

  e.preventDefault()

  if ($('#applicant-reg-form input[type="file"].file-size-over').length > 0){
    $('input[type="file"]').focus()
    return false;
  }

  var m_form=new FormData($('#applicant-reg-form')[0])


  m_form.append('csrfmiddlewaretoken',csrftoken)

  var intrested_list=[]
  $("input:checkbox[name='Interested']:checked").each(function(){
    intrested_list.push($(this).val());
  });

  m_form.append('intrested_in',JSON.stringify(intrested_list))
  //inspectForm(m_form)


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
          text: 'Thank you for registering your interest to attend Next World Forum. Please expect to receive an email from the Next World team',
          showConfirmButton: true,


        })

            setTimeout(() => {
              $('#applicant-reg-form')[0].reset()
              // window.location.href=window.location.origin

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

function check_file_input_size(el) {




  if (el.files[0].size / (1024*1024) < 1 && el.files[0] != null ){
    console.log(' no over size')
    $('#'+el.id+'-error').addClass('d-none')
    $('#'+el.id).removeClass('file-size-over')
    return true
  }
  else{
    console.log('over size', el.id)
    $('#'+el.id+'-error').html('please upload less than 3mb file')
    $('#'+el.id).addClass('file-size-over')
    $('#'+el.id+'-error').removeClass('d-none')
    return false
  }
  
  
}
$(document).ready(function () {
  $("#country").select2({
    placeholder: "Select a country",
  templateResult: formatCountry,
    data: isoCountries,
    theme:'bootstrap-5',
    
   
  }).on('change', function() {
    
    if (!this.checkValidity()){
      $('#'+this.id+'-error').removeClass('d-none')
     }
     else{
      $('#'+this.id+'-error').addClass('d-none')
     }
    
  });


 
  
});


function formatCountry (country) {
  if (!country.id) { return country.text; }
  var country = $(
    '<span class="flag-icon flag-icon-'+ country.iso.toLowerCase() +' flag-icon-squared"></span>' +
    '<span class="flag-text">'+ country.text+"</span>"
  );
  return country;
};


async function check_code_is_valid(code) {
  
  const response =await fetch('check_valid_code',{method: "POST", headers: {'X-CSRFToken': csrftoken,'Content-Type':'application/json'},
  body:JSON.stringify({'code':code})})

  const data=await response.json();

  return data

}

function check_code_is_valid_button() {

 

  check_code_is_valid($('#code-inp').val()).then(res => {

    if (res.valid){
      //forward
      $('.unique-code-div').hide()
      $('.main-div').show()
         $('#invited-head').show()

    }
    else{
      //give error meesage 
      text_reason_1=`Please note the access code you have entered is invalid or has already been used.` 

      text_reason_2= `If you require any assistance, please contact invitations@nextwrld.sa`

      $('#code-message').html(text_reason_1)
    //   $('#code-message-2').html(text_reason_2)
      
      $('.unique-code-div').show()
      $('.main-div').hide()
       $('#invited-head').hide()
    }

  })


}

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