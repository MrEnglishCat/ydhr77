let counter = 2;

$(document).ready(function () {
    $("#addInput").click(function () {
        $('#inputs').append(
            `<input type="text" name="input${counter}" placeholder="Имя">`
        );
        counter++;
    });
});