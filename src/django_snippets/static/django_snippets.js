window.addEventListener("load", f);
const maxLenghtTitle = 63
const maxLenghtDescription = 160

function f() {
    (($) => {

        init_snippet($)

        $(document).on('formset:added', (event, $row, formsetName) => {
            console.log(11233333333333)
            if (formsetName === 'author_set') {
                // Do something
            }
        });

        $(document).on('formset:removed', (event, $row, formsetName) => {
            // Row removed
        })
    })(django.jQuery);
}

function init_snippet($) {
    let snippet = $('#DjangoSnippet')
    let field_name_description = snippet.data().description
    let field_name_title = snippet.data().title

    let text_1 = $('#id_text_1').val()
    console.log($('<div>').append(text_1).find('h1').length)
    console.log($('<div>').append(text_1).find('h1').text())

    let title_listen = $(`#id_${field_name_title}`)
    let title = snippet.find('.sTitle')
    let titleCount = snippet.find('.sTitleCount')
    title.text(Slice(title_listen.val()))
    titleCount.text(title_listen.val().length)

    let description_listen = $(`#id_${field_name_description}`)
    let description = snippet.find('.sDescription')
    let descriptionCount = snippet.find('.sDescriptionCount')
    description.text(description_listen.val())
    descriptionCount.text(description_listen.val().length)

    title_listen.bind('input', (event) => {
        title.text(Slice(event.target.value))
        titleCount.text(event.target.value.length)
    })

    description_listen.bind('input', (event) => {
        description.text(event.target.value)
        descriptionCount.text(event.target.value.length)
    })
}

function Slice(val) {
    if (val.length > maxLenghtTitle) {
        console.log(val)
        return val.substr(0, maxLenghtTitle) + '...'
    } else {
        return val
    }
}

function title_() {

}

