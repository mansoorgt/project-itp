
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

            Swal.fire({
                position: 'top-center',
                icon: 'success',
                title: 'Your registration has been submited',
                showConfirmButton: false,
                timer: 1500

              })

              setTimeout(() => {

                window.location.href=window.location.origin

              }, 2000);
            
        }
    });
    
}