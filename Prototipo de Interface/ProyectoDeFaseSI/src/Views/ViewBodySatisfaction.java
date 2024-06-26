package Views;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JCheckBox;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ViewBodySatisfaction extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();
	private JTextField textField;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			ViewBodySatisfaction dialog = new ViewBodySatisfaction();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(false);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public ViewBodySatisfaction() {
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		{
			JLabel lblNewLabel = new JLabel("Su IMC es : ");
			lblNewLabel.setBounds(6, 6, 192, 16);
			contentPanel.add(lblNewLabel);
		}
		{
			JLabel lblNewLabel_1 = new JLabel("Edad ");
			lblNewLabel_1.setBounds(6, 51, 61, 16);
			contentPanel.add(lblNewLabel_1);
		}
		{
			textField = new JTextField();
			textField.setBounds(61, 46, 130, 26);
			contentPanel.add(textField);
			textField.setColumns(10);
		}
		{
			JLabel lblNewLabel_2 = new JLabel("Estas satisfecho con tu imagen corporal?");
			lblNewLabel_2.setBounds(6, 96, 409, 16);
			contentPanel.add(lblNewLabel_2);
		}
		
		JCheckBox chckbxNewCheckBox = new JCheckBox("Si");
		chckbxNewCheckBox.setBounds(70, 124, 128, 23);
		contentPanel.add(chckbxNewCheckBox);
		
		JCheckBox chckbxNo = new JCheckBox("No");
		chckbxNo.setBounds(70, 153, 128, 23);
		contentPanel.add(chckbxNo);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton btnRetroceder = new JButton("Retroceder");
				btnRetroceder.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						ViewIMC view = new ViewIMC();
						contentPanel.setVisible(false);
						view.setVisible(true);
					}
				});
				btnRetroceder.setActionCommand("OK");
				buttonPane.add(btnRetroceder);
				getRootPane().setDefaultButton(btnRetroceder);
			}
			{
				JButton btnContinuar = new JButton("Continuar");
				btnContinuar.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						ViewMedicalCondition view = new ViewMedicalCondition();
						getContentPane().setVisible(false);
						view.setVisible(true);
					}
				});
				btnContinuar.setActionCommand("Continuar");
				buttonPane.add(btnContinuar);
			}
		}
	}
}
