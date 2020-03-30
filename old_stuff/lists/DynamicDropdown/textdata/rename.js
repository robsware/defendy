function SetData(){
   var select = document.getElementById('agent');
   var agent_id = select.options[select.selectedIndex].value;
   document.myform.action = "index.php?action=contact_agent&agent_id="+agent_id ; # or .getAttribute('action')
   myform.submit();
}