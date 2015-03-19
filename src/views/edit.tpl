<!DOCTYPE html>
<html>
  <body>
    <form method="post" class="form" action="/edit">
      <input type="hidden" name="id" value="{{_id}}"/>
      Name: <input type="text" name="name" value="{{name}}"/><br>
      Email: <input type="text" name="email" value="{{email}}"/><br>
      <input type="submit" value="Edit Guest"/>
    </form>
  </body>
</html>
