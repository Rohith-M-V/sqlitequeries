import java.sql.*;

public class jdbc {
	public static void main(String args[]) throws Exception
	{
		//connecting to database
		String url = "jdbc:mysql://localhost:3306/mulesoft";
		String uname = "root";
		String pass = "Rohith.mv2001@";
		
		//query
		
		String query = "select * from movies";
		
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con = DriverManager.getConnection(url,uname,pass);
		Statement st = con.createStatement();
		ResultSet rs = st.executeQuery(query);
		
		
		String userData = "";
		while(rs.next())
		{
			userData = rs.getString(1) + "    " + rs.getString(2) + "    " + rs.getString(3) +"    " +  rs.getString(4) + "    " + rs.getInt(5);
			System.out.println(userData);
		}
		st.close();
		con.close();
	}
}
