var $newPart = `
    <table>
        {{ part_form.as_table }}
    </table>
`;

$('#addMore').on('click', function(){
    $('#partTable').after($newPart);
});
