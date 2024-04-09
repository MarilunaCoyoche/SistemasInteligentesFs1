package Views;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class ViewIMC extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JTextField txtPeso;
	private JTextField txtAltura;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			ViewIMC dialog = new ViewIMC();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public ViewIMC() {
		setTitle("CALCULAR IMC");
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		{
			JLabel lblNewLabel = new JLabel("Peso : ");
			lblNewLabel.setBounds(6, 18, 61, 16);
			contentPanel.add(lblNewLabel);
		}
		{
			JLabel lblNewLabel_1 = new JLabel("Altura : ");
			lblNewLabel_1.setBounds(6, 57, 61, 16);
			contentPanel.add(lblNewLabel_1);
		}
		
		txtPeso = new JTextField();
		txtPeso.setBounds(69, 8, 130, 26);
		contentPanel.add(txtPeso);
		txtPeso.setColumns(10);
		
		txtAltura = new JTextField();
		txtAltura.setBounds(69, 46, 130, 26);
		contentPanel.add(txtAltura);
		txtAltura.setColumns(10);
		
		JButton btnCalcularIMC = new JButton("Calcular IMC");
		btnCalcularIMC.setBounds(145, 84, 117, 29);
		contentPanel.add(btnCalcularIMC);
		
		JLabel ResultadoIMC = new JLabel("IMC : ");
		ResultadoIMC.setBounds(113, 125, 61, 16);
		contentPanel.add(ResultadoIMC);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton cancelButton = new JButton("Continuar");
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}
}
