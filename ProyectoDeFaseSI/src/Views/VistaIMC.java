package Views;
import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;

public class VistaIMC {

	private JFrame frame;
	private JTextField txtPeso;
	private JTextField txtAltura;
	private JLabel lblNewLabel;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					VistaIMC window = new VistaIMC();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public VistaIMC() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		txtPeso = new JTextField();
		txtPeso.setBounds(62, 6, 95, 26);
		frame.getContentPane().add(txtPeso);
		txtPeso.setColumns(10);
		
		txtAltura = new JTextField();
		txtAltura.setColumns(10);
		txtAltura.setBounds(232, 6, 90, 26);
		frame.getContentPane().add(txtAltura);
		
		JLabel lblPeso = new JLabel("Peso");
		lblPeso.setBounds(14, 11, 36, 16);
		frame.getContentPane().add(lblPeso);
		
		lblNewLabel = new JLabel("Altura");
		lblNewLabel.setBounds(185, 11, 45, 16);
		frame.getContentPane().add(lblNewLabel);
	}
}
