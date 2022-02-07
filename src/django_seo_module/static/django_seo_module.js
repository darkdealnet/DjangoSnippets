window.addEventListener("load", f);
const maxLenghtTitle = 63
const maxLenghtDescription = 160

function f() {
    (($) => {
        if ($('body.change-form').length) {
            init_snippet($)
        } else if ($('body.change-list').length) {
            console.log('change-list')
        }
        $(document).on('formset:added', (event, $row, formsetName) => {
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
    let snippet_description = snippet.find('.sDescription')
    let title = $('#id_title')
    let description = $('#id_description')
    let header = $('#id_header')
    let titleIsChange = false
    let titleIsBlank = title.val().length === 0


    if (title.val().length !== 0) {
        snippet_title.text(Slice(title.val()))
    }
    snippet_description.text(description.val())

    title.bind('input', (event) => {
        if (event.type) {
            titleIsChange = true
            snippet_title.text(Slice(event.target.value))
            return
        }
        if (!titleIsBlank) {
            snippet_title.text(Slice(event.target.value))
        }
    })

    description.bind('input', (event) => {
        snippet_description.text(event.target.value)
    })

    header.bind('input', (event) => {
        if (titleIsBlank) {
            snippet_title.text(event.target.value)
        }
        if (titleIsBlank && !titleIsChange) {
            title.val(event.target.value)
        }

        if (event.target.value.length === 0) {
            titleIsBlank = true
            titleIsChange = false
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


// let text_1 = $('#id_text_1').val()
// console.log($('<div>').append(text_1).find('h1').length)
// console.log($('<div>').append(text_1).find('h1').text())
// title.text(Slice(title_listen.val()))
// description.text(description_listen.val())