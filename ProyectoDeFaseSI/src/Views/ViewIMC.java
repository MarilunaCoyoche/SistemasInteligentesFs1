package Views;
import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;

public class ViewIMC {

	private JFrame frmCalcularImc;
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
					ViewIMC window = new ViewIMC();
					window.frmCalcularImc.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public ViewIMC() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmCalcularImc = new JFrame();
		frmCalcularImc.setTitle("Calcular IMC");
		frmCalcularImc.setBounds(100, 100, 450, 107);
		frmCalcularImc.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmCalcularImc.getContentPane().setLayout(null);
		
		txtPeso = new JTextField();
		txtPeso.setBounds(62, 6, 95, 26);
		frmCalcularImc.getContentPane().add(txtPeso);
		txtPeso.setColumns(10);
		
		txtAltura = new JTextField();
		txtAltura.setColumns(10);
		txtAltura.setBounds(219, 6, 90, 26);
		frmCalcularImc.getContentPane().add(txtAltura);
		
		JLabel lblPeso = new JLabel("Peso");
		lblPeso.setBounds(14, 11, 36, 16);
		frmCalcularImc.getContentPane().add(lblPeso);
		
		lblNewLabel = new JLabel("Altura");
		lblNewLabel.setBounds(169, 11, 45, 16);
		frmCalcularImc.getContentPane().add(lblNewLabel);
		
		JButton btnCalcularImc = new JButton("Calcular IMC");
		btnCalcularImc.setBounds(321, 6, 117, 29);
		frmCalcularImc.getContentPane().add(btnCalcularImc);
		
		JLabel lblResultadoImc = new JLabel("Resultado IMC : ");
		lblResultadoImc.setBounds(14, 44, 292, 16);
		frmCalcularImc.getContentPane().add(lblResultadoImc);
	}
}
