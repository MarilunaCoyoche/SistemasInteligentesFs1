package Views;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;

public class ViewPhysicalActivity extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			ViewPhysicalActivity dialog = new ViewPhysicalActivity();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public ViewPhysicalActivity() {
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		{
			JLabel lblNewLabel = new JLabel("Cual es tu nivel de Actividad Fisica ");
			lblNewLabel.setBounds(20, 16, 337, 16);
			contentPanel.add(lblNewLabel);
		}
		{
			JCheckBox chbxSedentario = new JCheckBox("Sedentario (Poco o nada de ejercicio)");
			chbxSedentario.setBounds(20, 57, 300, 23);
			contentPanel.add(chbxSedentario);
		}
		{
			JCheckBox chbxLigero = new JCheckBox("Ligera (Ejercicio 2-3 dias por semana)");
			chbxLigero.setBounds(20, 92, 300, 23);
			contentPanel.add(chbxLigero);
		}
		{
			JCheckBox chboxModerado = new JCheckBox("Moderada (Ejercicio 4-5 dias por semana)");
			chboxModerado.setBounds(20, 127, 300, 23);
			contentPanel.add(chboxModerado);
		}
		{
			JCheckBox chbxAlto = new JCheckBox("Alta (Ejercicio 6-7 dias por semana)");
			chbxAlto.setBounds(20, 162, 300, 23);
			contentPanel.add(chbxAlto);
		}
		{
			JCheckBox chbxAtleta = new JCheckBox("Atleta Profesional (Ejercicio Intenso 6-7 dias por semana)");
			chbxAtleta.setBounds(20, 197, 424, 23);
			contentPanel.add(chbxAtleta);
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("Retroceder");
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Continuar");
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}
}
