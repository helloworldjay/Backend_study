package exam;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class TenServlet
 */
@WebServlet("/Ten") //url 부분
public class TenServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public TenServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// 브라우저가 들어온 컨텐츠가 이미지인지 영상인지 등을 확인하는 코드
		response.setContentType("text/html;charset=utf-8");
		// printWriter 객체를 return 받는 메소드
	    PrintWriter out = response.getWriter();
	    out.println("<h1>1-10까지 출력!!</h1>");
	    for(int i = 1; i <11; i++) {
	    	out.print(i+"<br>");
	    	
	    }
	    out.close();
		
		
	}

}
