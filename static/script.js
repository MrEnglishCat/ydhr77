let counter = 2;

$(document).ready(function () {
    $("#addInput").click(function () {
        alert(counter);
        $('#inputs').append(
            `<input type="text" name="input${counter}" placeholder="Имя">`
        );
        counter++;
    });
});