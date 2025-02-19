/**
 * Add a LI element to a list when the user clicks
 * on the tag DIV#add_item
 */
$(document).ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<li>Item</li>');
  });
});
