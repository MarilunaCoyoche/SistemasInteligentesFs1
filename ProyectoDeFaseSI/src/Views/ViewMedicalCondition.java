package Views;

import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JCheckBox;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class ViewMedicalCondition extends JDialog {

	private static final long serialVersionUID = 1L;
	private final JPanel contentPanel = new JPanel();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			ViewMedicalCondition dialog = new ViewMedicalCondition();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(false);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public ViewMedicalCondition() {
		setBounds(100, 100, 450, 300);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		{
			JLabel lblNewLabel = new JLabel("Tienes alguna condicion medica que afecte su peso?");
			lblNewLabel.setBounds(23, 20, 395, 16);
			contentPanel.add(lblNewLabel);
		}
		{
			JCheckBox chboxSi = new JCheckBox("Si");
			chboxSi.setBounds(168, 63, 128, 23);
			contentPanel.add(chboxSi);
		}
		{
			JCheckBox chboxNo = new JCheckBox("No");
			chboxNo.setBounds(168, 104, 128, 23);
			contentPanel.add(chboxNo);
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("Retroceder");
				okButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						ViewBodySatisfaction view = new ViewBodySatisfaction();
						contentPanel.setVisible(false);
						view.setVisible(true);
					}
				});
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Continuar");
				cancelButton.addActionListener(new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						contentPanel.setVisible(false);
						ViewPhysicalActivity view = new ViewPhysicalActivity();
						view.setVisible(true);
					}
				});
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}

}
