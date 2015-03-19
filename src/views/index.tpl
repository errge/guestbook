<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to MongoDB!</title>
    <style type="text/css">
      h5 {display: inline;}
      .label {text-align: right}
      .guestbook {float:left; padding-top: 10px;}
      .name {width:100%;float:left; padding:3px;}
      .wrapper { padding-left: 25px; padding-top: 20px}
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Welcome To MongoDB!</h1>
      <div class="guestbook_input" >
      <form method="post" class="form" action="/new">
        Name: <input type="text" name="name"/><br>
        Email: <input type="text" name="email"/><br>
        <input type="submit" value='Add Guest'/>
      </form>
      </div>
      <div class="guestbook">
        <h3>Guests:</h3>
        <table border=1>
          <tr><th>Name<th>Email<th>Operations
          %for entry in entries:
          <tr>
            <td>{{entry['name']}}
            <td>{{entry['email']}}
            <td>
              <a href="/delete?id={{entry['_id']}}">delete</a>
              <a href="/editform?id={{entry['_id']}}">edit</a>
          %end
        </table>
      </div>
    </div>
  </body>
</html>
