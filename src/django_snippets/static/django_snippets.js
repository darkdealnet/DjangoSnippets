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
    let snippet_title = snippet.find('.sTitle')
    let title_listen = $(`#id_${snippet.data().title}`)
    let title = $('#id_title')

    let description = snippet.find('.sDescription')
    let description_listen = $(`#id_${snippet.data().description}`)
    let header_listen = $('#id_header')

    let state = {
        titleIsBlank: title.val().length === 0,
        titleIsChange: false
    }

    function init_title() {
        if (title.val().length !== 0) {
            snippet_title.text(Slice(title.val()))
        }
    }

    init_title()

    // let text_1 = $('#id_text_1').val()
    // console.log($('<div>').append(text_1).find('h1').length)
    // console.log($('<div>').append(text_1).find('h1').text())

    // title.text(Slice(title_listen.val()))
    // description.text(description_listen.val())

    // слушатели

    title_listen.bind('input', (event) => {
        if (!state.titleIsBlank) {
            snippet_title.text(Slice(event.target.value))
        }
    })

    // description_listen.bind('input', (event) => {
    //     description.text(event.target.value)
    // })
    //

    header_listen.bind('input', (event) => {
        if (state.titleIsBlank) {
            snippet_title.text(event.target.value)
        }
        if (state.titleIsBlank) {
            title.val(event.target.value)
        }

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

