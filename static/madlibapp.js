$(document).ready(function () {
    const $body = $("body");
    const $input1 = $("#input1-label")
    const $input2 = $("#input2-label")
    const $input3 = $("#input3-label")
    const $input4 = $("#input4-label")
    const $input5 = $("#input5-label")
    const $storyDesc = $("#story-desc");
    const submit = document.querySelector("#madlib-form");
    const select = document.querySelector("#story-theme");



    select.addEventListener("change", function () {

        if (this.value == "1") {
            $storyDesc.show();
            $input1.text("Name A [place]")
            $input2.text("Name A [noun]")
            $input3.text("Name A [verb]")
            $input4.text("Name An [adjective]")
            $input5.text("Name A [plural-noun]")

            $storyDesc.text("Once upon a time, long ago in {place}, there lived a" + 
            " large {adjective} {noun}. It loved to {verb} {plural_noun}.");
        }
        
        if (this.value == "2") {
            $storyDesc.show();
            $input1.text("Name An [adjective]")
            $input2.text("Name A [science term]")
            $input3.text("Name A [verb]")
            $input4.text("Name An [adjective]")
            $input5.text("Name A [plural-noun]")

            $storyDesc.text("As a(n) {adjective} astronaut, I completely understand the laws of" +
                " {science term}, therefore, I am able to {verb} very well! This makes me a(n) {adjective}"
                + " candidate to work on {plural-noun}")
        }
        if (this.value == "3") {
            $storyDesc.show();
            $input1.text("Name A [verb ending in 'ing']")
            $input2.text("Name An [adjective]")
            $input3.text("Name A [noun]")
            $input4.text("Name A [verb ending in 'ing']")
            $input5.text("Name A [verb: past-tense]")

            $storyDesc.text("While {verb ending in 'ing'} in the ocean, I came across a(n) {adjective}"
                + " looking sea-{noun}. Instead of {verb ending in 'ing'}, I decided to approach it."
                + " Afterwards, I never {verb: past-tense} again!")
        }
        if (this.value == "4") {
            $storyDesc.show();
            $input1.text("Name An [adjective]")
            $input2.text("Name An [adjective]")
            $input3.text("Name A [plural-noun]")
            $input4.text("Name A [verb]")
            $input5.text("Name An [adverb]")

            $storyDesc.text("The Amazon Rain-Forest is so {adjective}! I mean, someone can easily get"
                + " {adjective}. In the Amazon, there are so many deadily {plural-noun} as well. If you"
                + " {verb} fast enough, you will be able to {adverb} fend them off")
        }
       
    })


})
