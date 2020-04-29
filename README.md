<h2>Recreating bug</h2>

<ol>
  <li>Clone this repository into your folder</li>
  <li>Activate python3 shell from the folder you're in</li>
  <li>Import WebStickerGame class from the sticker_bug_recreator.py</li>
  <li>Instantiate an instance of a WebStickerGame Class (It takes one parameter - number of 'rounds')</li>
  <li>Call WebStickerGame's 'remove_cards' method (with 2 parameters: row_number & number_of_cards 
  (example: remove_cards(1, 1)))</li>
</ol>


You see (via print methods) that a card was removed from <strong>all</strong> Igra instances.
Only cards that SHOULD be removed are the ones from the 1st igra instance (with the ID of 0.)

To understand the problem, however you must first study the code yourself.
