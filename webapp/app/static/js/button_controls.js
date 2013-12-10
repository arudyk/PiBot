$(document).ready(function(){
  $('.sitebody').keydown(function(event){    
      if(event.keyCode==87){
         $('#forward').trigger('click');
         console.log("w");
      }
  });
});
